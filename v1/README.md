# pdf2ko (version.1)

pdf2ko is a program which translates pdf file to Korean and save it as text file.


## Prerequisite
- OS : macOS
- brew
```
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```
- python3
``$ brew install python3``

- PyPDF2
``$ pip3 install PyPDF2``

## Directory

The directory tree is like below.

```
v1
+-- src
|	+--translate.py
+-- before_trans
|   +-- [your_pdf].pdf
+-- after_trans
|   +-- [translated_file].txt
```


## Let's translate !
Clone the repository. Make sure you are in ``v1/src/`` folder.
 Command will be like this:

```
$ cd /pdf2ko/v1/src
```
Let's assume a test pdf file 'test.pdf' is in ``v1/before_trans`` directory.
Execute translate.py.
When asked to give a file name, type the file name without extensions.

```
$ python3 traslate.py
File name to translate: test
```
Then, it will process the pdf file and translate into Korean.
```
...
Saved into ../after_trans/out_test.txt
```
The translated file will be located at ``v1/after_trans`` folder.


