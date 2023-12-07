FROM python:3.11

RUN mkdir /shop

WORKDIR /shop

COPY requirements.txt /shop/

RUN pip install -r requirements.txt

ADD . /shop/

