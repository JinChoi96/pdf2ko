import os, sys
import PyPDF2

srcFolder = '../before_trans/'
destFolder = '../after_trans/'

fileName = input("File name to translate : ")
print("Range to translate")
f = int(input("From: "))
to = int(input("To: "))

outFile = destFolder+'out_'+fileName+'.txt'

pdfFileObj = open(srcFolder+fileName+'.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pages = pdfReader.numPages

if(to>pages):
    print("Please enter a number less than "+str(to))
    sys.exit()

for i in range(f-1, to):
    pageObj = pdfReader.getPage(i)

    print("Page No: ", i+1)

    text = pageObj.extractText()
    #text = text.replace("\n", " ")
    print(text)

    #os.system('echo \"'+text+'\" | trans -brief >> ' + outFile)
    print()


print("Saved into "+outFile)
pdfFileObj.close()
