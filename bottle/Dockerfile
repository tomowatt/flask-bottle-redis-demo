FROM python:3.9.8-alpine

WORKDIR /app/
COPY requirements.txt .
RUN pip3 install --requirement requirements.txt --no-cache-dir

WORKDIR /app/src/
COPY /src/ .

EXPOSE 8080

ENTRYPOINT [ "gunicorn" ]
CMD [ "api:app", "--bind=0.0.0.0:8080" ]