FROM python:3.10

WORKDIR /srv
COPY requirements.txt .
COPY mkdocs.yml .
RUN pip install -r requirements.txt

CMD mkdocs serve -a 0.0.0.0:8000
