FROM centos/python-38-centos7:latest

USER root
RUN yum install -y unzip
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install
RUN rm awscliv2.zip
RUN rm -rf ./aws
RUN yum install -y gcc
RUN yum install -y python3-devel
RUN yum install -y postgresql-libs
RUN yum install -y postgresql-devel


WORKDIR /service

ARG BUILD_MODE
COPY ./docker/aws/aws_${BUILD_MODE}.py /service
COPY ./docker/aws/zappa_settings.json /service

RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install awslambdaric
RUN venv/bin/pip install aws-wsgi
RUN venv/bin/pip install zappa
COPY ./project/requirements.txt ./
RUN venv/bin/pip install -r requirements.txt

CMD ["zappa deploy dev"]
