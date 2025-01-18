FROM python:3.11.8-bookworm

RUN apt-get update && apt-get install -y --no-install-recommends && \
    pip install --upgrade pip && \
    apt-get clean

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

ENV RABBITMQ_URL="."
ENV QUEUE='.'

EXPOSE 8010

CMD ["uvicorn", "app:app", "--port", "8010", "--host", "0.0.0.0", "--log-level", "critical"]