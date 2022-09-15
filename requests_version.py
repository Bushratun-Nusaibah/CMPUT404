import requests 

#print (requests.__version__)

#res = requests.get("http://www.google.com/")
#print(res)

raw_url = "https://raw.githubusercontent.com/Bushratun-Nusaibah/CMPUT404/main/requests_version.py"

res = requests.get(raw_url)
print(res.text)