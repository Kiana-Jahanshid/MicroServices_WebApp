FROM python

WORKDIR /app  
COPY . .
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["uvicorn", "app:app","--proxy-headers" , "--host", "0.0.0.0", "--port", "5000"]