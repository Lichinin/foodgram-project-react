FROM python:3.7-slim

WORKDIR /app

COPY . ./

RUN python -m pip install --upgrade pip
RUN apt-get update && apt-get install -y pkg-config libcairo2-dev build-essential
RUN pip3 install --no-cache-dir -r requirements.txt
RUN mkdir -p /app/logs
RUN chmod 777 /app/logs

CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000" ]