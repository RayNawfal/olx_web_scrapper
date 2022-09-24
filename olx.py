import requests
import os
import bs4

url = 'https://www.olx.com.lb/ads/q-mercedes/?sorting=desc-price'


print("downloading page ... %s..." % url)
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'lxml')
# find all ul classes between featured and normal ads
Entries = soup.find_all("ul", class_ = "ba608fb8 de8df3a3")
# select all entries inside the normal ads
Elements = Entries[1].find_all("li", class_ = "c46f3bfe")
# print out info for each element of normal ads
for Element in Elements:
    Title = Element.find('div', {"aria-label": "Title"}).get_text()
    Element = Element.find('div', {"aria-label": "Price"}).get_text()
    print(Title)
    print(Element)
    print("\n")
