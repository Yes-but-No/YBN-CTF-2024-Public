FROM python:alpine
WORKDIR /app
COPY . .
RUN apk add socat
ENV FLAG="YBN{y0u_h4v3_f0uND_Y0uR_w4Y_ou+_0f_+H1$_M4Z3_YAY_a7e717e6507}"
CMD ["socat", "TCP-LISTEN:10003,reuseaddr,fork", "EXEC:python3 /app/maze.py"]
