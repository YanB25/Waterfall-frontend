FROM nginx

# File Author / Maintainer
MAINTAINER yanbin "yanb25@mail2.sysu.edu.cn"

COPY ./dist/* /usr/share/nginx/html/

COPY ./static/* /usr/share/nginx/html/static/
# Copy custom configuration file from the current directory
COPY nginx.conf /etc/nginx/nginx.conf

expose 80