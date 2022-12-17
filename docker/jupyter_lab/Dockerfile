FROM jupyter/datascience-notebook

WORKDIR /notebook

COPY ./docker/jupyter_lab/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
