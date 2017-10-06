#!/bin/sh

echo "Update TZ"
cp /usr/share/zoneinfo/$TZ /etc/localtime
echo $TZ > /etc/timezone

if [ ! -f /etc/dhparams/dhparams.pem ]; then
    echo "Generate dhparams.pem"
    openssl dhparam -out /etc/dhparams/dhparams.pem 2048
fi

sed -i "s|NGINX_HOST|${NGINX_HOST}|g" /etc/nginx/conf.d/http.conf
sed -i "s|NGINX_HOST|${NGINX_HOST}|g" /etc/nginx/conf.d/https.conf
mv -v /etc/nginx/conf.d/https.conf /tmp/https.conf

(
    sleep 5
    while :
    do
        if openssl x509 -checkend 86400 -noout -in /etc/letsencrypt/live/$NGINX_HOST/fullchain.pem; then
            echo "Certs are OK"
        else
            echo "Get certs"
            certbot certonly -t -n --agree-tos --renew-by-default --email "${LE_EMAIL}" --webroot -w /usr/share/nginx/html -d $NGINX_HOST
        fi
        cp -vf /tmp/https.conf /etc/nginx/conf.d/https.conf
        nginx -s reload
        sleep 86400
    done
) &


echo "Start Nginx"
nginx -g "daemon off;"
