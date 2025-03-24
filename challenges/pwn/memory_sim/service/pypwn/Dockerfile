FROM python:3.11-slim-bookworm

RUN apt update
RUN apt install -y socat

WORKDIR /challenge

COPY chall.py .

EXPOSE 1337

USER nobody

CMD ["socat", "TCP-LISTEN:1337,reuseaddr,fork", "EXEC:python3 -u ./chall.py,pty,stderr"]
