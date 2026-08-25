FROM caddy:2-alpine AS caddy

FROM python:3.10

WORKDIR /srv
COPY --from=caddy /usr/bin/caddy /usr/bin/caddy
COPY . .
RUN pip install -r requirements.txt

ENTRYPOINT ["/bin/sh", "/srv/entrypoint.sh"]