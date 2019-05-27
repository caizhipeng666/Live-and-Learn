# Gitlab-Ci
> 针对某个需要做CI/CD的项目，需要将代码库的该设置打开，并为其配置 gitlab-runner
https://www.jianshu.com/p/d63d9941565f
```
sudo docker pull gitlab/gitlab-runner
```
```
sudo docker run -d --name gitlab-runner --restart always \
    -v /srv/gitlab-runner/config:/etc/gitlab-runner \
    -v /var/run/docker.sock:/var/run/docker.sock \
    gitlab/gitlab-runner:latest
```
在容器中执行register操作，将gitlab上的项目注册到gitlab-runner中：
```
sudo docker exec -it gitlab-runner gitlab-ci-multi-runner register
```
stages:
  - build
  - test
  - deploy
  - restart
