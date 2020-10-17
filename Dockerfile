FROM python:3.7-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN ["adduser", "whelp_user", "--disabled-password", "--ingroup", "www-data", "--quiet"]

RUN apt-get update && apt-get -y dist-upgrade
RUN apt-get -y install build-essential libssl-dev libffi-dev libblas3 libc6 liblapack3 gcc python3-dev python3-pip cython3
RUN apt install -y netcat
COPY ./entrypoint.sh /home/whelp_user/entrypoint.sh
RUN chmod +x /home/whelp_user/entrypoint.sh

USER whelp_user

ADD whelp/ /home/whelp_user/whelp
WORKDIR /home/whelp_user/whelp

ENV PATH="/home/whelp_user/.local/bin:${PATH}:/usr/local/python3/bin"

RUN pip install --user --upgrade pip
RUN pip install --user -r requirements.txt

ENTRYPOINT ["/home/whelp_user/entrypoint.sh"]
