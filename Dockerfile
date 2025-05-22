FROM python:3.10
WORKDIR /srv
# COPY requirements.txt .
# Copy all
COPY . .
RUN pip install -r requirements.txt

CMD mkdocs serve -a 0.0.0.0:8000
