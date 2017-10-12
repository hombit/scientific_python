FROM python:3

MAINTAINER Konstantin Malanchev <malanchev@physics.msu.ru>

ENV PROJECT /scpysai
RUN mkdir -pv $PROJECT
WORKDIR $PROJECT

COPY . $PROJECT
RUN python setup.py install

CMD ["python", "bin/sci_py_example"]
