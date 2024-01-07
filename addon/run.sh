#!/usr/bin/env bashio
set -e

ML_API_TOKEN=$(bashio::config 'obico_api_secret')
PORT=$(bashio::addon.port 3333)

venv/bin/gunicorn --bind "0.0.0.0:$PORT" --workers 1 wsgi
