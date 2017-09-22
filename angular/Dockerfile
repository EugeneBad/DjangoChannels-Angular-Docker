FROM nginx:latest
COPY ./dist /var/www
RUN mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.template
COPY ./test.conf /etc/nginx/conf.d
WORKDIR /var/www
