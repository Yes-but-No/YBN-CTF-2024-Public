#!/bin/sh

export LD_PRELOAD=/srv/lib/x86_64-linux-gnu/libc.so.6
export LD_LIBRARY_PATH=/srv/lib/x86_64-linux-gnu
exec /srv/lib64/ld-linux-x86-64.so.2 --library-path /srv/lib/x86_64-linux-gnu /srv/app/chall "$@"
