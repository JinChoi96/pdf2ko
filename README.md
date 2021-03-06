# pdf2ko - v2

pdf2ko is a program which translates a pdf file to Korean and save it as a text file. 

Originally made for my sister who is having hard time with research survey. 

Future versions will be more automated. 


## Prerequisites
- OS : macOS
- brew
```
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```
- git  
``$ brew install git``
- python3  
``$ brew install python3``
- PyPDF2  
  ``$ pip3 install PyPDF2`` 
- translate-shell (For translation, pdf2ko uses [translate-shell](https://github.com/soimort/translate-shell))  

  ``$ brew install translate-shell`` 


## Directory

The directory tree is like below.

```
v2
+-- src
| +-- translate.py
+-- before_trans
| +-- [your_pdf].pdf
+-- after_trans
| +-- [translated_file].txt
```


## Let's translate !
Clone the repository. Make sure you are in ``v2/src/`` folder.
 Command will be like this:

```
$ git clone https://github.com/JinChoi96/pdf2ko.git
$ cd /pdf2ko/v2/src
```
Put your pdf file which will be translated to in ``v2/before_trans`` folder. We assume 'test.pdf' file as for an example.  
Execute translate.py. When asked to give a file name, type the file name without extensions.  

```
$ python3 traslate.py
File name to translate: test
Range to translate
From: 1
To : 3
```
Then, it will process the pdf file and translate into Korean.
```
...
Saved into ../after_trans/out_test.txt
```
The translated file will be located at ``v2/after_trans/`` folder.


### Note 
Since translate-shell is not supposed to used as a library, frequent request will block your IP and prevent to use translation from Google.   

Use only when translating appropriate quantity.  