FROM jupyter/datascience-notebook


COPY ./docker/jupyter_lab/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# ENTRYPOINT ["start-notebook.sh"," --NotebookApp.token=''"]
