import os
import PyPDF2

basePath = '../before_trans/'
outputPath = '../after_trans/'
fileName = input("File name to translate : ")
#fileName = fileName + '.pdf'
pdfFileObj = open(basePath+fileName+'.pdf', 'rb')
w = open(outputPath+"out_"+fileName+'.txt', 'a')
outFile = outputPath+"out_"+fileName+".txt"
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pages = pdfReader.numPages

for i in range(pages):
    pageObj = pdfReader.getPage(i)

    print("Page No: ", i)

    text = pageObj.extractText()
    text = text.replace("\n", " ")
    print(text)
    #w.write("Page No:"+str(i))
    os.system('echo \"'+text+'\" | trans -brief >> ' +outputPath+"out_"+fileName+'.txt')
    #for i in range(len(text)):
     #   print(text[i])

    print()

    #w.write(text+"\n")

print("Saved into "+outputPath+"out_"+fileName+".txt")
pdfFileObj.close()
