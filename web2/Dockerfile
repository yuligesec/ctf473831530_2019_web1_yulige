FROM ubuntu:16.04

RUN sed -i "s/http:\/\/archive.ubuntu.com/http:\/\/mirrors.aliyun.com/g" /etc/apt/sources.list
RUN apt-get update && apt-get install -y \
    python3  iputils-ping net-tools curl netcat-traditional \
    python3-pip

RUN pip3 install flask
RUN echo "export HINT='mysql_user_is_yuligeeee123321'" >> /etc/profile
WORKDIR /var/www/yuligeeeeeee/
ADD ./app.py /var/www/yuligeeeeeee/
COPY ./start.sh /etc
RUN chmod u+x /etc/start.sh
RUN useradd -m ctf
RUN chown -R root:ctf /var/www/yuligeeeeeee/
RUN chmod -R 755 /var/www/yuligeeeeeee/

EXPOSE 8080

