FROM python:3.8-slim

WORKDIR /service

RUN pip install --upgrade pip
RUN pip install pytest
RUN apt-get update
RUN apt-get install -y libpq-dev
RUN apt-get install -y gcc

EXPOSE 8000

CMD ["/bin/sh"]
