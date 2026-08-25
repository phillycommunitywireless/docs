FROM caddy:2-alpine AS caddy

FROM python:3.10

WORKDIR /srv
COPY --from=caddy /usr/bin/caddy /usr/bin/caddy
COPY . .
RUN pip install -r requirements.txt

RUN ["chmod", "+x", "/usr/bin/caddy"]
RUN ["chmod", "+x", "/srv/entrypoint.sh"]
ENTRYPOINT ["/bin/sh", "/srv/entrypoint.sh"]