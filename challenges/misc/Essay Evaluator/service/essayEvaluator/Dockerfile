FROM python:3.11-slim
WORKDIR /app

RUN useradd -m ctfuser
RUN apt update
RUN apt install -y socat

COPY . /app
RUN chmod -R 555 /app

USER ctfuser

ENTRYPOINT ["sh"]
CMD [ "/app/entry.sh" ]
