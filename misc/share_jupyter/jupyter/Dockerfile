FROM jupyter/minimal-notebook

RUN conda install --yes astropy matplotlib numpy scipy pandas

COPY jupyter_notebook_config.py $HOME/.jupyter/
COPY custom.js $HOME/.jupyter/custom/
USER root
RUN chown -R jovyan $HOME/.jupyter
USER jovyan

WORKDIR $HOME/work

EXPOSE 8000
