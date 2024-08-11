FROM python


WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

CMD ["uvicorn", "your-app.main:app", "--host", "0.0.0.0", "--port", "80"]