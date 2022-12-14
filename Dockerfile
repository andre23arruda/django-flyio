FROM python:3.10.0-slim-buster
ENV LANG C.UTF-8

RUN apt-get -y update && apt-get -y autoremove

RUN mkdir /app
WORKDIR /app

RUN apt-get install -y python python-pip python-dev

ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
ADD . /app
RUN python manage.py collectstatic --noinput

EXPOSE 8000
# CMD ["gunicorn", "setup.wsgi", "-b", "0.0.0.0:8000", "--access-logfile", "-"]
CMD ["/bin/bash", "-c", "python manage.py collectstatic --noinput; gunicorn --bind :8000 --workers 1 setup.wsgi"]
