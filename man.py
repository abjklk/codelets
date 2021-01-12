import requests

url = ""
ct = 0
for i in range(1,41):
	for j in range(1,50):
		# print(url+str(i)+"/"+"{:03d}".format(j)+".jpg")
		a = requests.get(url+str(i)+"/"+"{:03d}".format(j)+".jpg")
		if a.status_code != 200:
			print("no")
			break
		print(i,j)
		ct+=1
		f = open(f"x/{ct}.jpg","wb")
		f.write(a.content)
		f.close()