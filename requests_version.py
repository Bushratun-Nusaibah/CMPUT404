import requests 

#this is for the first part of the lab exercise  
#print (requests.__version__)

#this was for question 5 of the lab 
#res = requests.get("http://www.google.com/")
#print(res)

raw_url = "https://raw.githubusercontent.com/Bushratun-Nusaibah/CMPUT404/main/requests_version.py"

res = requests.get(raw_url)
print(res.text)