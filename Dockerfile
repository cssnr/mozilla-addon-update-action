FROM python:3.13-alpine

COPY src/main.py /main.py

ENTRYPOINT ["python", "/main.py"]
