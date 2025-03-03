FROM python:3.13-alpine

COPY src/ /src

ENTRYPOINT ["python", "/src/main.py"]
