import PyPDF2
pdfFileObj = open('z.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
count = 0
arr = list()
for x in range(1, 551):
    pageObj = pdfReader.getPage(x)
    a = pageObj.extractText()
    a = a.split('\n')
    for i in a:
        if i.isnumeric():
            count += 1
            if(count % 2 == 0):
                i = int(i)
                arr.append(i)

newarr = list()
for d in arr:
    if (d >  0 and d <= 100):
        newarr.append(d)
newarr.sort(reverse=True)
print(newarr)
print(newarr.__len__())
