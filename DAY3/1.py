##step 0:
import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com/"

## step 1:
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

##step 2 :
soup = BeautifulSoup(htmlContent , 'html.parser')
print(soup)
# print(soup.prettify)          ##"prettify se code clean way mai show hota h"

##step 3:
## get the title of HTML page
title = soup.title

print(type(soup))           # BeautifulSoup object display hoga 
print(type(title))          # Tag  object display hoga 
print(type(title.string))   # NavigableString object display hoga

## get all the paragraph from the page
paras = soup.find_all('p')
print(paras)

## get all the anchor tags from the page
anchors = soup.find_all('a')
print(anchors)

## get first elements in HTML page
print(soup.find('p'))       #isse first paragraph mil jayega

##Get classes of any element in the HTML page 
print(soup.find('p')['class'])       #isse first paragraph ki classes mil jayega

## find all the elements with class lead
print(soup.find_all('p' , class_= 'lead'))

## get the text from the tags/soups
print(soup.find('p').get_text())

## Get all the links on the page :
for link in anchors :
    print(link.get('href'))

##4. Comments
markup = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup)
print(soup2.p)