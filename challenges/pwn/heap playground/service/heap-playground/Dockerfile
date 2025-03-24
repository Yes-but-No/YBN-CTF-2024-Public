FROM pwn.red/jail

COPY --from=debian@sha256:0eb754294a949430923ed0fef02b6661954399d01e83ceb5f839e00139e79a96 / /srv
COPY flag.txt /srv/app/flag.txt
COPY playground /srv/app/run
RUN chmod +x /srv/app/run
