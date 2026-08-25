#!/bin/sh
# entrypoint.sh
set -e

if [ "$APP_TAG" = "production" ]; then
    echo "Starting in Production Mode..." && mkdocs build && exec caddy run --config Caddyfile --adapter caddyfile
else
    echo "Starting in Development Mode..." && exec mkdocs serve -f mkdocs.dev.yml -a 0.0.0.0:8000
fi
