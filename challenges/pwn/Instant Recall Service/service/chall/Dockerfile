FROM pwn.red/jail

COPY --from=debian / /srv
COPY flag.txt /srv/app/flag.txt
COPY chall /srv/app/run
RUN chmod +x /srv/app/run

