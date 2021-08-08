FROM python:3.7.1

LABEL Author="SemSysGroup30"
LABEL version="1.0.0"

ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_APP "app.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True

RUN mkdir /app
WORKDIR /app


RUN pip install flask requests

ADD . /app

EXPOSE 5000

CMD flask run --host=0.0.0.0
