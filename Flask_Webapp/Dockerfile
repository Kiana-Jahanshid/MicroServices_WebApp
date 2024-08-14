FROM python

WORKDIR /app

COPY . /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8080

CMD ["quart", "run", "--port=8080", "--host=0.0.0.0"]