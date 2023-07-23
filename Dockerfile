FROM python:3.10
MAINTAINER mohamad

ENV PYTHONUNBUFFERED 1

RUN mkdir /net_utils
COPY . /net_utils
WORKDIR /net_utils
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt
