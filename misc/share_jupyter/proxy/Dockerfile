FROM nginx:alpine

MAINTAINER Konstantin Malanchev <hombit@gmail.com>

RUN apk add  --update certbot tzdata openssl && \
    rm -rf /var/cache/apk/*

COPY ./docker-entrypoint.sh /docker-entrypoint.sh

RUN rm /etc/nginx/conf.d/default.conf
COPY ./*.conf /etc/nginx/conf.d/


ENTRYPOINT ["/docker-entrypoint.sh"]
