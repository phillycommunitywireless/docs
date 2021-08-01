FROM python:3
WORKDIR docs
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD mkdocs serve -a 0.0.0.0:8000

