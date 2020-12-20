import requests
from bs4 import BeautifulSoup

n = str(input("masukkan link/url: "))

url = n

#membuat requests
r = requests.get(url)
#hasil response
request = r.content

filename = "tes.txt"
f = open(filename, "w")

headers = "sumber : "+ url + "\n"

f.write(headers)

soup = BeautifulSoup(request, 'html.parser')
#extract element
title = soup.find_all('a', attrs={'class':'bookTitle'})
author = soup.find_all('a', attrs={'class':'authorName'})

count = 0
for x in range(0, len(title)):
    count += 1
    print("{0}.  {1}\n   -{2}".format(count, title[x].text.strip(), author[x].text.strip()))
