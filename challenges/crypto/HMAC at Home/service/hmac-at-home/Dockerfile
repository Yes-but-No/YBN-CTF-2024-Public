FROM python:3.11-alpine

RUN apk add --no-cache socat=1.8.0.0-r0

WORKDIR /challenge

COPY flag.txt .
COPY main.py .

EXPOSE 1337

USER nobody

CMD ["socat", "TCP-LISTEN:1337,reuseaddr,fork", "EXEC:python3 -u ./main.py,pty,stderr"]