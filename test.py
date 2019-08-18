import PyPDF2
import time
start_time = time.time()


def main():
    pdfFileObj = open('med.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pages = 453
    count = 0
    for x in range(pages):
        pageObj = pdfReader.getPage(x)
        a = pageObj.extractText()
        a = a.split(' ')
        for i in a:
            if ('OPN' in i):
                count += 1
    print('count is ',count)
    print(a)
    pdfFileObj.close()


main()
print("--- %s seconds ---" % (time.time() - start_time))
