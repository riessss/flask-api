FROM python:3.10-slim

COPY . requirements.txt

RUN pip install -r --no-cache requirements.txt

COPY . .

CMD ["python","main.py"]