import requests
import json

url = "http://data.coa.gov.tw/Service/OpenData/FromM/FarmTransData.aspx?cropCode=fd1"
data = requests.get(url).json()

#print (data)
