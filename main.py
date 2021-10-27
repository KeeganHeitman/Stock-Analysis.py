import BeautifulSoup,tkinter,MediaWiki,lmxl
with open("index.html") as fp:
  soup=BeautifulSoup(fp,'lmxl')
soup=BeautifulSoup("<html>a web page<html>","lmxl")
