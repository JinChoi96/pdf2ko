import os
import PyPDF2

srcFolder = '../before_trans/'
destFolder = '../after_trans/'

fileName = input("File name to translate : ")
outFile = destFolder+'out_'+fileName+'.txt'

pdfFileObj = open(srcFolder+fileName+'.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pages = pdfReader.numPages

for i in range(pages):
    pageObj = pdfReader.getPage(i)

    print("Page No: ", i)

    text = pageObj.extractText()
    text = text.replace("\n", " ")
    print(text)

    os.system('echo \"'+text+'\" | trans -brief >> ' + outFile)
    print()


print("Saved into "+outFile)
pdfFileObj.close()
