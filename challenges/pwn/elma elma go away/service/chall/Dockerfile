# Step 7/16 : RUN useradd -m -s /bin/bash ctfuser &&     echo 'ctfuser:ctfpassword' | chpasswd &&     mkdir /home/ctfuser/challenge &&     chown -R root:ctfuser /home/ctfuser/challenge &&     chmod 555 /home/ctfuser/challenge

FROM ubuntu:latest

SHELL ["/bin/bash", "-c"]


RUN apt-get update && \
    apt-get install -y gnupg2 curl && \
    apt-get update && \
    apt-get install -y socat && \
    rm -rf /var/lib/apt/lists/*

RUN chmod +x /bin/sh /bin/bash

COPY ./libc.so.6 /x86_64-linux-gnu/libc.so.6
COPY ./ld-linux-x86-64.so.2 /x86_64-linux-gnu/ld-linux-x86-64.so.2
RUN chown root:root /x86_64-linux-gnu/libc.so.6 /x86_64-linux-gnu/ld-linux-x86-64.so.2
RUN chmod 755 /x86_64-linux-gnu/libc.so.6 /x86_64-linux-gnu/ld-linux-x86-64.so.2
RUN cp /x86_64-linux-gnu/* /lib/x86_64-linux-gnu/


RUN useradd -m -s /bin/bash ctfuser && \
    echo 'ctfuser:ctfpassword' | chpasswd && \
    mkdir /home/ctfuser/challenge && \
    chown -R root:ctfuser /home/ctfuser/challenge && \
    chmod 555 /home/ctfuser/challenge

COPY ./chall /home/ctfuser/challenge/
RUN chmod 555 /home/ctfuser/challenge/chall

COPY ./flag.txt /home/ctfuser/challenge/
RUN chmod 444 /home/ctfuser/challenge/flag.txt


RUN chmod 555 /home/ctfuser && \
    chown -R root:ctfuser /home/ctfuser/challenge && \
    chmod 555 /home/ctfuser/challenge && \
    chown root:ctfuser /home/ctfuser/.bashrc && chmod 444 /home/ctfuser/.bashrc


RUN chsh -s /bin/rbash ctfuser
RUN chmod 700 /home/ctfuser

WORKDIR /home/ctfuser/challenge
USER ctfuser 

CMD socat TCP-LISTEN:8000,reuseaddr,fork EXEC:"/home/ctfuser/challenge/chall,stderr"
