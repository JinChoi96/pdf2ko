import os, sys
import PyPDF2
import pdf2txt

srcFolder = '../before_trans/'
destFolder = '../after_trans/'

fileName = input("File name to translate : ")
print("Range to translate")
f = int(input("From: "))
to = int(input("To: "))

inFile = srcFolder+fileName+'.pdf'
midFile = srcFolder+'mid_'+fileName
outFile = destFolder+'out_'+fileName+'.txt'

os.system("python3 pdf2txt.py "+inFile+" --page-numbers "+str(f)+" "+str(to)+ " >> "+midFile)

f = open(midFile, 'r')
text = f.read()
text = text.replace("\n", " ")
text = text.replace("  ", "\n")

os.system('echo \"'+text+'\" | trans -brief >> ' + outFile)

print("Translation is done!")
