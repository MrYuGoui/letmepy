import requests
from fake_useragent import UserAgent
UA=UserAgent()
proxies={
    "http":"http://74.116.59.8:53281"
}
res=requests.get(url="http://icanhazip.com")
#114.249.34.253
if res.text.replace("\n","")=="114.249.34.253":
    print("代理未生效")
else:
    print(res.text)