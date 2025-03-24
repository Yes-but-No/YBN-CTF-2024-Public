FROM python:3.11-slim-bookworm

WORKDIR /chall

RUN pip3 install pycryptodome
COPY Hero-3-source.py .
COPY ynetd .
# I've lost my mind here
RUN chmod +x Hero-3-source.py # probably dont need this anymore.... right?
RUN chmod +x ynetd

EXPOSE 1337

CMD ./ynetd -p 1337 "python3 Hero-3-source.py"
