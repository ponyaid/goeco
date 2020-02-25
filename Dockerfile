FROM python:3.7-alpine

COPY ./requirements.txt /goeco/requirements.txt

WORKDIR /goeco

RUN pip install -r requirements.txt

COPY . /goeco

EXPOSE 5000

CMD [ "gunicorn", "app:app", "-b", "0.0.0.0:5000" ]
