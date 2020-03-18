# Base image for Jupyter
FROM jupyter/minimal-notebook

# Install required Python packages
RUN conda install --yes astropy astroquery matplotlib numpy scipy pandas \
    lmfit scikit-learn pillow scikit-image requests photutils cython \
    numba requests beautifulsoup4 flask

# Install TeX and ffmpeg for matplotlib
USER root
RUN apt-get update && \
    apt-get install -y texlive-lang-cyrillic dvipng ffmpeg && \
    apt-get clean -y &&\
    rm -rvf /var/lib/apt/lists/* &&\
    truncate -s 0 /var/log/*log
USER jovyan

# Copy configuration into image
COPY jupyter_notebook_config.py $HOME/.jupyter/
COPY custom.js $HOME/.jupyter/custom/
USER root
RUN chown -R jovyan $HOME/.jupyter
USER jovyan

WORKDIR $HOME/work

EXPOSE 8000
