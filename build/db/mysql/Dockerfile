FROM mysql:latest

COPY ./build/db/mysql/my.cnf /etc/mysql/conf.d/my.cnf

# install locales
RUN apt-get clean \
    && apt-get update \
    && apt-get install -y locales locales-all \
    # compile local file
    && locale-gen ja_JP.UTF-8

# set lang=Ja.utf-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:en
ENV LC_ALL ja_JP.UTF-8

# change TZ to Ja
RUN ln -sf /usr/share/zoneinfo/Japan /etc/localtime