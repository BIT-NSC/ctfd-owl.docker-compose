# docker-nginx-php7-fpm
自定义WEB环境 By XiaBee

#### 目录结构

```
.
├── docker-compose.yml
├── docker-compose-no-dynamic.yml
├── flag
├── nginx
│   └── nginx.conf
├── php
│   ├── Dockerfile
│   ├── php-fpm.conf
│   └── php.ini
├── README.md
└── www
    └── index.php
```

#### 单独搭建

`docker-compose-no-dynamic.yml`用于非动态容器

```shell
docker-compose up -d
curl localhost:9999
```

#### 用于CTFd的`ctfd-owl`或`ctfd-whale`动态容器插件

`fl0g`为主目录下的`flag`文件，`docker-compose.yml`的 `net` 网络名称记得与 CTFd 的 frp containers 网段一致

注意填写正确的使用 frpc 转发的端口: `80` (和 `docker-compose` 中 `service` 的 `expose` 一致)

`php`和`nginx`的配置按照题目自行变更

#### 站点目录:

`./www`

