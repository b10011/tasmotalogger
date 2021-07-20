FROM python:3.9.6-slim-buster

RUN apt update && \
    DEBIAN_FRONTEND=noninteractive apt -y install cron

COPY ./entrypoint.sh /app/entrypoint
COPY ./execute.sh /app/execute
COPY ./main.py /app/main.py
COPY ./requirements.txt /app/requirements.txt

RUN pip3 install --no-cache-dir -r /app/requirements.txt

RUN chmod +x /app/entrypoint /app/execute

CMD ["/app/entrypoint"]
