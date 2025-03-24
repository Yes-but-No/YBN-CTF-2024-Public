FROM alpine:3.20

RUN apk add --no-cache socat=1.8.0.0-r0

EXPOSE 10003

CMD ["socat", "TCP-LISTEN:10003,reuseaddr,fork", "EXEC:echo 'YBN24{c@t5_IN_NEts_W1th_haTS_@ND_b4ts}'"]