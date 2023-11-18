FROM python:3.8

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

COPY . /app

WORKDIR /app

RUN pip install --no-cache -r requirements.txt

CMD ["python", "main.py"]