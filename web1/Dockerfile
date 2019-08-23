FROM ubuntu:16.04
ENV DEBIAN_FRONTEND noninteractive
RUN   apt-get -y update && \ 
      apt-get -y  install iputils-ping net-tools curl netcat-traditional php-curl php7.0-curl php-http-request2 php-picofeed apache2 php-mysql php mysql-client vim libapache2-mod-php && \
      apt-get -y  autoremove  && \ 
      rm -rf /var/lib/apt/lists/* 
COPY ./start.sh /start.sh

RUN chmod +x /start.sh
COPY ./flag.php /var/www/html
COPY ./index.php /var/www/html
RUN rm /var/www/html/index.html
    
EXPOSE 80
CMD ["/start.sh"]

