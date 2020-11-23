FROM python:3.9.0-alpine

WORKDIR /app/
COPY requirements.txt .
RUN pip3 install --requirement requirements.txt --no-cache-dir

WORKDIR /app/src/
COPY /src/ .

EXPOSE 8080

ENTRYPOINT [ "gunicorn" ]
CMD [ "demo:app", "--bind=0.0.0.0:8080" ]