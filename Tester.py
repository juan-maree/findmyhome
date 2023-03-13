
# coding: utf-8

# ## Imports

# In[2]:


import requests
from bs4 import BeautifulSoup
import json
from pandas import DataFrame as df


# In[29]:


def scrape_properties(url, page):
    page = requests.get(url % page)
    soup = BeautifulSoup(page.text, 'html.parser')
    results = soup.find_all(class_ = 'listingResult row')
    properties = []

    for i in results:
        title = i.find("a",{"class":"title"})
        properties.append({
            'price': i.find(class_ = 'priceDescription').contents[0][2:].replace(" ", ""),
            'suburb': i.find(class_ = 'suburb').contents[0],
            'href': i.attrs['href']
        })
    return properties


    


# In[45]:


page = 1
end_flag = False
raw_data = []
while not end_flag:
    result = scrape_properties('https://www.privateproperty.co.za/for-sale/western-cape/cape-town/cape-town-city-bowl/59?tp=2500000&page=%s', page)
    if len(result) > 0:
        page = page + 1
        raw_data = raw_data + result
    else:
        end_flag = True
data = df(raw_data)
print(data)

