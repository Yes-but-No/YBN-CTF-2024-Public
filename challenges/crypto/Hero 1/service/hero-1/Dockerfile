FROM python:3.11-slim-bookworm

WORKDIR /chall

RUN pip3 install pycryptodome
COPY Hero_1_source.py .
COPY ynetd .
# I'm losing my mind here
RUN chmod +x Hero_1_source.py # probably dont need this anymore.... right?
RUN chmod +x ynetd

EXPOSE 1337

CMD ./ynetd -p 1337 "python3 Hero_1_source.py"
