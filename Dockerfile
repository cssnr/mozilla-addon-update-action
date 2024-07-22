FROM python:3.11-alpine

COPY src/main.py /main.py

ENTRYPOINT ["python", "/main.py"]
