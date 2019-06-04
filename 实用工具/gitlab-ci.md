# Gitlab-Ci
> https://docs.gitlab.com/runner/install/linux-manually.html
1. 注册
```
pass
```
2. 配置
> https://docs.gitlab.com/runner/register/index.html
### sudo gitlab-runner register
```

```
3. .gitlab-ci.yml
```
stages:
  - test

test:
  stage: test
  tags:
    - test
  before_script:
    - export TZ=Asia/Shanghai
    - export DJANGO_SETTINGS_MODULE=XXX.test
    - pip install -r requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
  script:
    - python manage.py check
    - python manage.py test --setting='XXX.test' -v3
```
> ✔注意这里的tags必须和注册时的gitlab-ci tags相同
