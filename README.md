# Face Analysis Website

its a website , containing :
+ object detection microservice 
+ Face Analysis microservice
+ flask web app micriservice
+ postgresql  

 


# How to install 

```
pip install -r requirements.txt
```

# How to run in local :

firt we have to run 2 first microservices :

## FaceAnalysis with FASTAPI
```
uvicorn main:app --reload
```
## Object Detection with flask :

```
flask run
```

## webapp with flask :
```
quart --app app run --port 8080
```

# Result 


+ app link :
```
https://webapplication.liara.run/
```
