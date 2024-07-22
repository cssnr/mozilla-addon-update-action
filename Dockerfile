FROM python:3.11-alpine

COPY docker-entrypoint.sh /
COPY src/ /src

ENTRYPOINT ["sh", "/docker-entrypoint.sh"]
