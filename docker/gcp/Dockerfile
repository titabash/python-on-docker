FROM python:3.8-slim
WORKDIR /service
ARG BUILD_MODE
COPY ./docker/gcp/gcp_${BUILD_MODE}.py /service/

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get -y install libpq-dev
RUN apt-get -y install gcc
RUN mkdir ./site-packages
RUN pip install --upgrade pip
# google cloud
RUN pip install google-cloud
RUN pip install functions-framework
COPY ./project/requirements.txt ./
RUN pip install -r requirements.txt

EXPOSE 8010

CMD ["/bin/sh"]
