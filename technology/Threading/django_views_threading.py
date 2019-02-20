# coding: utf8
"""在Django添加多线程组件"""
import threading
from functools import partial


class ThreadManager(object):
    def __init__(self):
        self.reset()

    def activate_thread(self, key, func, *args):
        print('[enter thread] ', key)
        partial_func = partial(func, *args)
        t = RequestThread(key, self.async_res, partial_func)
        t.start()
        self.thread_list.append(t)

    def wait_res(self, timeout=60):
        for t in self.thread_list:
            t.join(timeout)

        return self.async_res

    def reset(self):
        self.thread_list = []
        self.async_res = {}


class RequestThread(threading.Thread):
    def __init__(self, key, res_dict, func):
        super(RequestThread, self).__init__()
        self.key = key
        self.res_dict = res_dict
        self.func = func

    def run(self):
        res = self.func()
        self.res_dict[self.key] = res
        return


# 调用案例
def lecture_analysis(request, lecture_id):
    '''数据中心, 用多线程保证速度'''
    thread_manager = ThreadManager()

    lecture = Lecture.objects.using('slave').get(id=lecture_id)

    # 总览
    thread_manager.activate_thread('total', lecture_total_data_func, lecture)

    # 完课率
    thread_manager.activate_thread(
        'complete_rate',
        lecture_total_meta_data_func,
        lecture,
        'complete_rate'
    )
    # 性别比
    thread_manager.activate_thread(
        'sexual_rate',
        lecture_total_meta_data_func,
        lecture,
        'sexual_rate'
    )
    # 新老用户比
    # thread_manager.activate_thread(
    #     'new_old_rate',
    #     lecture_total_meta_data_func,
    #     lecture,
    #     'new_old_rate'
    # )
    # 邀请明细
    thread_manager.activate_thread(
        'invite',
        lecture_invite_data_func,
        lecture
    )
    # 渠道明细
    thread_manager.activate_thread(
        'source',
        lecture_source_data_func,
        lecture
    )
    # 打赏明细
    thread_manager.activate_thread(
        'reward',
        lecture_reward_lecturer_data_func,
        lecture
    )

    _data = thread_manager.wait_res()

    pay_sexual_rate = lecture.get_pay_sexual_rate()
    pay_sexual_rate = [
        {'value': pay_sexual_rate['male'], 'name': '男性'},
        {'value': pay_sexual_rate['female'], 'name': '女性'},
        {'value': pay_sexual_rate['agender'], 'name': '无性别'}
    ]

    total_data = {
        'total': _data.get('total', {}),
        'complete_rate': _data.get('complete_rate', {}),
        'sexual_rate': _data.get('sexual_rate', {}),
        'new_old_rate': _data.get('new_old_rate', {}),
        'pay_sexual_rate': pay_sexual_rate,
        'reward': _data.get('reward', {}),
    }

    promote_data = {
        'invite': _data.get('invite', {}),
        'source': _data.get('source', {}),
    }
    promote_data['source']['list_data'] = promote_data['source']['sources'] if promote_data['source'] else []
    promote_data['invite']['list_data'] = promote_data['invite']['list_data'] if promote_data['invite'] else []

    for v in promote_data['source']['list_data']:
        v['v'] = v.copy()

    for v in promote_data['invite']['list_data']:
        v['v'] = v.copy()

    return render(request, 'crm2/analysis.html', {
        'total_data': total_data,
        'lecture': lecture,
        'promote_data': promote_data
    })
