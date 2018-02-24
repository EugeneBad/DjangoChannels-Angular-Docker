FROM nginx:latest
RUN mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.template
COPY ./nginx_conf/main_lb.conf /etc/nginx/conf.d
WORKDIR /var/www
