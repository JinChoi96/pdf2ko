import os, sys
import PyPDF2
import re
import pdf2txt

srcFolder = '../before_trans/'
destFolder = '../after_trans/'

fileName = input("File name to translate : ")
print("Range to translate")
f = int(input("From: "))
to = int(input("To: "))

pageNoList = [i for i in range(f, to+1)]
pageNoStr = ""
for no in pageNoList:
    pageNoStr += str(no)+ " "


inFile = srcFolder+fileName+'.pdf'
midFile = srcFolder+'mid_'+fileName+'.txt'
outFile = destFolder+'out_'+fileName+'.txt'

os.system("python3 pdf2txt.py "+inFile+" --page-numbers "+pageNoStr+"  >> "+midFile)

substituteFrom = ["\n"]
substituteTo = [" "]
delimeter = "#$%"

f = open(midFile, 'r')
text = f.read()

for (fr, to) in zip(substituteFrom, substituteTo):
    text = text.replace(fr, to)

text = text.replace("  ", delimeter)
texts = text.split("delimeter")

for t in texts:
    os.system('echo \"'+t+'\" | trans -brief >> ' + outFile)

print("Saved into "+outFile)
