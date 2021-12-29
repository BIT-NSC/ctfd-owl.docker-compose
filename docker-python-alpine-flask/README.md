# docker-python-alpine-flask
自定义apline下的Python Flask环境 By SpaceSkyNet

#### 目录结构

```
.
├── docker-compose.yml
├── flag
├── flask
│   ├── Dockerfile
│   └── app.py
└── www
    └── app.py
```

#### 单独搭建

`docker-compose-no-dynamic.yml`用于非动态容器

```shell
docker-compose up -d
curl localhost:8000
```

#### 用于CTFd的`ctfd-owl`或`ctfd-whale`动态容器插件

`fl0g`为主目录下的`flag`文件，`docker-compose.yml`的 `net` 网络名称记得与 CTFd 的 frp containers 网段一致

注意填写正确的使用 frpc 转发的端口: `8000` (和 `docker-compose` 中 `service` 的 `expose` 一致)

`service`的配置按照题目自行变更

#### 站点目录:

`./www`

