FROM ubuntu:16.04
ENV DEBIAN_FRONTEND noninteractive
RUN   apt-get  update && \
      apt-get -y  install curl vim mysql-client mysql-server iputils-ping net-tools netcat-traditional && \
      apt-get   autoremove  && \
      rm -rf /var/lib/apt/lists/* \
      && /etc/init.d/mysql start \
      && mysqladmin -uroot password yuLIgeeeeeee666+++

COPY ./start.sh /start.sh
COPY ./init.sql /init.sql
RUN chmod +x /start.sh
#set database
RUN set -x \
    && /etc/init.d/mysql start  \
	&& mysql  -e "create user yuligeeee123321 identified by '';"  -uroot  -pyuLIgeeeeeee666+++ \ 
	&& mysql -e "grant select on fla4441111g.* to 'yuligeeee123321'@'%' identified by '' WITH GRANT OPTION;"  -uroot -pyuLIgeeeeeee666+++ \ 
	&& mysql -e "flush privileges;" -uroot -pyuLIgeeeeeee666+++ \
    && mysql -e "source /init.sql;"  -uroot -pyuLIgeeeeeee666+++ \
    && rm /init.sql 
RUN sed -i 's/bind-address/#bind-address/g' /etc/mysql/mysql.conf.d/mysqld.cnf

EXPOSE 3306
CMD ["/start.sh"]


