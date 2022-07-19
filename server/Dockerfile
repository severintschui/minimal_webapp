FROM python:3.10.5

COPY src /usr/src

WORKDIR /usr/src

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uwsgi", "--ini", "uwsgi.ini"]
