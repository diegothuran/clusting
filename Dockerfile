FROM ubuntu:16.04

MAINTAINER Diego Santos

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y python python-pip
#RUN apt-get install libmysqlclient-dev

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir logs

RUN python -m nltk.downloader wordnet pros_cons reuters stopwords rslp punkt

ENTRYPOINT ["/docker-entrypoint.sh"]
