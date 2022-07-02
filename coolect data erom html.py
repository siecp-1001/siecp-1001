from cgitb import html
from urllib import response
import urllib.request as urllip2
from bs4 import BeautifulSoup 
response = urllip2.urlopen('http://192.168.1.246/home.htm')
html_doc=response.read()
soup =BeautifulSoup(html_doc,'html.parser')
strhtm= soup.prettify()
print(strhtm[:1000])
print(soup.title)
print(soup.title.string)
print(soup.a.string)
print(soup.b.string)
