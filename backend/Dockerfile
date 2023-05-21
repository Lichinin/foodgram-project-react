FROM python:3.7-slim

RUN apt-get update && apt-get install -y pkg-config libcairo2-dev build-essential

WORKDIR /app

COPY backend/requirements.txt ./

RUN python -m pip install --upgrade pip
RUN pip3 install --no-cache-dir -r ./requirements.txt

COPY . ./

CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000" ]