# docker-pwn-ubuntu-16.04

自定义 pwn 环境 By SpaceSkyNet, 基于[ctftraining/base_pwn_xinetd](https://github.com/ctftraining/base_pwn_xinetd)

#### 目录结构

```
.
├──docker-compose.yml
├──Dockerfile
├──flag
├──README.md
├──src
│  └──pwn
└──tcpdump
```

#### 可执行文件目录:

`./src`

#### 单独搭建

`docker-compose-no-dynamic.yml`用于非动态容器

```shell
docker-compose up -d
nc localhost 9999
```

#### 用于CTFd的`ctfd-owl`或`ctfd-whale`动态容器插件

`fl0g`为主目录下的`flag`文件，`docker-compose.yml`的 `net` 网络名称记得与 CTFd 的 frp containers 网段一致

注意填写正确的使用 frpc 转发的端口: `10000` (和 `docker-compose` 中 `service` 的 `expose` 一致)

`service`的配置按照题目自行变更