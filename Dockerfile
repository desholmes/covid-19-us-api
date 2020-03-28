FROM python:3.7.6-slim

WORKDIR /usr/src

COPY covid_19_us/ ./covid_19_us
COPY data/ ./data
COPY manage.py .
COPY gunicorn.py .
COPY requirements.txt .
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

RUN pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT ["bash", "/usr/src/entrypoint.sh"]