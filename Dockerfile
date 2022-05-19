FROM python:3.9.2-slim-buster

WORKDIR /app-run

COPY ./requirements.txt ./requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

RUN pip install -e .
RUN chmod +x entrypoint.sh

ENV GUNICORN_WORKERS 2

EXPOSE 5000

ENTRYPOINT ["sh", "entrypoint.sh"]

