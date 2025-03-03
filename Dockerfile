FROM python:3.13-alpine

LABEL org.opencontainers.image.source="https://github.com/cssnr/mozilla-addon-update-action"
LABEL org.opencontainers.image.description="Mozilla Addon Update Action"
LABEL org.opencontainers.image.authors="smashedr"

COPY src/ /src

ENTRYPOINT ["python", "/src/main.py"]
