FROM python:3.8-slim

WORKDIR /service

RUN pip install --upgrade pip
RUN pip install pytest
RUN apt-get update
RUN apt-get install -y libpq-dev
RUN apt-get install -y gcc
COPY ./project/requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8000

WORKDIR /service/src

CMD ["uvicorn", "api:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
