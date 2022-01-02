FROM amazon/aws-lambda-python

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


WORKDIR ${LAMBDA_TASK_ROOT}

ARG BUILD_MODE
COPY aws_${BUILD_MODE}.py ${LAMBDA_TASK_ROOT}

RUN mkdir ./site-packages
RUN pip install --upgrade pip
RUN pip install awslambdaric
RUN pip install aws-wsgi
