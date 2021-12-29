# docker-compose(s) for ctfd-owl problems

用于 BIT NSC 改版 `ctfd-owl`，略加修改应该可以用于`ctfd-whale`.

## 已有 docker-compose

```
Web:
nginx-mariadb-php7-fpm
nginx-php5.5-fpm
nginx-php7-fpm
python-alpine
python-alpine-flask

Pwn:
pwn-ubuntu-16.04
```

## 制作新的 docker-compose

### 目录结构

```
.
├── docker-compose.yml
├── *Dockerfile (not necessary, you can use the existing image)
├── flag
├── *service-need-to-build
│   ├── ...
│   └── Dockerfile
└── www
    ├── ...
    └── index.php(app.py/...)
```

### docker-compose

请一定注意`expose`的端口，并在建立 problem 时填写正确的端口.

example:

```docker-compose
version: "3"
services:
    service:  # nginx 之类服务的名称必须为 service
        image: nginx:latest
        volumes:
            - ./nginx:/etc/nginx/conf.d
            - ./www:/var/www/html
            # nginx和php必须同时映射才能通信
        restart: always
        environment: 
            TZ: Asia/Shanghai
        expose: # 提供web等服务的端口
            - "80"
        networks:
            - default
            - net
    
    php:
        image: xiabee/php7.3-fpm
        build: ./php
        volumes: 
            - ./php/php.ini:/usr/local/etc/php/php.ini
            - ./php/php-fpm.conf:/usr/local/etc/php-fpm.d/www.conf
            - ./www:/var/www/html
            - "$PWD/flag:/var/www/html/fl0g:ro"
            # nginx和php必须同时映射才能通信      
        environment: 
            TZ: Asia/Shanghai
        restart: always
        networks:
            - default

networks:
    # 配置docker network
    default: # 同一题目不同容器间通信
    net: # 和 frpc 进行通信，用于对外端口映射（仅提供web等服务的一个容器加入）
      external: 
         name: bitnsc_frp_containers
```