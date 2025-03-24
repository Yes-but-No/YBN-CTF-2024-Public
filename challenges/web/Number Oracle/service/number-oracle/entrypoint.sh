#!/bin/sh
set -eou pipefail

gunicorn wsgi:app \
  --bind '0.0.0.0:8000' \
  --workers=4