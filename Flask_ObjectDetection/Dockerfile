FROM python

WORKDIR /appf 

# COPY . /appf
COPY requirements.txt /appf
RUN pip install -r requirements.txt
# COPY . .
EXPOSE 5000
CMD ["flask" , "run" , "--host", "0.0.0.0", "--port", "5000"]