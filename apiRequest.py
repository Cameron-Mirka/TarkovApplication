import urllib.request
import json

def apiRequest():
    urllib.request.urlretrieve('https://tarkov-market.com/api/v1/items/all?x-api-key=7XNeqKL1SmtNW5L2','D:\TarkovJson\data.json')
    data = open('D:\TarkovJson\data.json','r',encoding="utf8")
    jasondata = data.read()
    obj = json.loads(jasondata)

    print(str(len(obj)) + ' items loaded from api')
    return obj

def apiFormat(data):
    print(data)