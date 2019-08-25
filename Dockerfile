FROM ubuntu:latest

MAINTAINER Filip Stysiak "stysiak.filip@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "currency_converter/run.py" ]
