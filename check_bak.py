import pathlib

html = open('frontend/index.html.bak', encoding='utf-8').read()
print('bak lines:', html.count(chr(10)))
