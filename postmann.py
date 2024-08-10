import requests

url = "http://127.0.0.1:8000/faceanalysis"
payload = {}
files=[
  ('file',('face.jpeg',open('Flask_Webapp/static/uploads/face.jpeg','rb'),'image/jpeg'))
]
headers = {}
response = requests.request("POST", url, headers=headers, data=payload, files=files , proxies={'http':'','https':''})
print(response.text)
print(response.json())
print(response.json()["genders"][0])



