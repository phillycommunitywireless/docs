#!/bin/sh
# entrypoint.sh
set -e

if [ "$APP_TAG" = "production" ]; then
    echo "Starting in Production Mode..." && mkdocs build && exec caddy run --config Caddyfile --adapter caddyfile
elif [ "$APP_TAG" = "deploy_preview" ]; then
    # Render-specific settings for deploy previews - they have their own webserver,
    # so generate prod files w/ mkdocs build, but don't serve w/ caddy.
    echo "Starting in Deploy Preview Mode..." && exec mkdocs serve -f mkdocs.yml -a 0.0.0.0:8000
else
    echo "Starting in Development Mode..." && exec mkdocs serve -f mkdocs.dev.yml -a 0.0.0.0:8000
fi
