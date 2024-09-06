FROM python:3.10

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

COPY /requirements/requirements.txt .

RUN pip install -r requirements.txt

COPY src .

RUN chmod a+x docker/*.sh
