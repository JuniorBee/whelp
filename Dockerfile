FROM python:3.7-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# DB vars
ENV DB_USER_NAME whelp_db_user
ENV DB_NAME whelp_db
ENV DB_HOST 127.0.0.1
ENV DB_PORT 5432
ENV DB_PASSWORD 9y87xkls32re2

ENV DJANGO_SECRET_KEY 4m0k0gaxtg9q1fhp@n%^c2h1=-tn4wfgrl%yo#!80c2@1-hx


RUN ["adduser", "whelp_user", "--disabled-password", "--ingroup", "www-data", "--quiet"]

USER whelp_user

ADD whelp/ /home/whelp_user/whelp
WORKDIR /home/whelp_user/whelp

ENV PATH="/home/whelp_user/.local/bin:${PATH}:/usr/local/python3/bin"

RUN pip install --user -r requirements.txt

CMD python manage.py runserver 0.0.0.0:8000
#CMD gunicorn whelp.wsgi:application --bind 0.0.0.0:8000
EXPOSE 8000
