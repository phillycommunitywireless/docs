FROM caddy:2-alpine AS caddy

FROM python:3.10

WORKDIR /srv
COPY --from=caddy /usr/bin/caddy /usr/bin/caddy
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["/bin/sh", "/srv/entrypoint.sh"]