FROM python:3.11 as base

RUN apt-get update && apt-get install -y
RUN pip install --upgrade pip
COPY . .

RUN pip3 install -r requirements.txt

ENV p 23
ENV q 7

CMD python3 main.py