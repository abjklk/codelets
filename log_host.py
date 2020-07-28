#!/usr/bin/env python3
import re
import csv
from collections import defaultdict
import operator

errDict = defaultdict(int)
userDict = defaultdict(list)

f = open("ticky.log","r")

for line in f.readlines():
	if re.search(r"ticky: INFO: ([\w \w]*)", line):
		# msg
		# print(re.findall(r"ticky: INFO: ([\w \w]*)", line)[0])
		# ticket id
		# print(re.findall(r"#[0-9]*", line)[0][1:])
		# username
		if userDict[(re.findall(r"\([A-Za-z]*", line)[0][1:])]:
			userDict[(re.findall(r"\([A-Za-z]*", line)[0][1:])][0]+=1
		else:
			userDict[(re.findall(r"\([A-Za-z]*", line)[0][1:])]=[1,0]
	else:
		# what went wrong
		errDict[(re.findall(r"ticky: ERROR: ([\w ]*) ", line)[0])]+=1
		# username
		if userDict[(re.findall(r"\([A-Za-z]*", line)[0][1:])]:
			userDict[(re.findall(r"\([A-Za-z]*", line)[0][1:])][1]+=1
		else:
			userDict[(re.findall(r"\([A-Za-z]*", line)[0][1:])]=[0,1]
f.close()

with open('error_messages.csv', 'w', newline='') as csvfile:
    fieldnames = ['error', 'count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in sorted(errDict.items(), key=operator.itemgetter(1), reverse=True):
    	writer.writerow({'error':i[0], 'count':i[1]})

with open('user_statistics.csv', 'w', newline='') as csvfile:
    fieldnames = ['username','info','error']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in sorted(userDict):
    	writer.writerow({'username':i, 'info':userDict[i][0], 'error':userDict[i][1]})
	