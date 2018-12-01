FROM python:3.7-alpine3.8
COPY . /app/
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "NaiveDictionaryService:app", "-b", ":8000"]
