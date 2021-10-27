import BeautifulSoup,tkinter,MediaWiki,lmxl
search=https://www.google.com/search?q=apple+stock
with open("index.html") as fp:
  soup=BeautifulSoup(fp,'lmxl')
soup=BeautifulSoup("search","lmxl")
