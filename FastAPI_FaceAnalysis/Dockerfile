FROM python

# WORKDIR /appface

WORKDIR /usr/src/app
COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /usr/src/requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app","--proxy-headers","--host", "0.0.0.0" , "--port", "8000"]
