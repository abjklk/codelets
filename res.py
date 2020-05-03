import requests

url = 'http://kletecheresults.contineo.in/index.php/component/report/?task=getReport&id=procard&usn=01FE17BME044'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
a = requests.get(url,headers=headers)
if a.status_code == 200:
	f = open(url[-6:]+'.pdf','w+b')
	f.write(a.content)
	f.close()