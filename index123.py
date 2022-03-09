import requests
from bs4 import BeautifulSoup as bs
import json

header={
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}

lst_pagens=[]
data=[]
for i in range(1,9):
    url=f'https://shop.casio.ru/catalog/?PAGEN_1={i}'
    lst_pagens.append(url)

for urls in lst_pagens:
    req=requests.get(urls,headers=header)
    content_web=req.content
    soup=bs(content_web,'lxml')

    articul=soup.find_all(class_='product-item__articul')
    price=soup.find_all(class_='product-item__price')
    link=soup.find_all(class_='product-item__link')
    
    c=0
    for a in link:
        href='https://shop.casio.ru/'+str(a.get('href').strip())
        dct={
            'Model':articul[c],
            'Price':price[c],
            'link':href
        }
        data.append(dct)
        c+=1



