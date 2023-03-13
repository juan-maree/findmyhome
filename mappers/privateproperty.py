# %%
import requests
from bs4 import BeautifulSoup
import json
from pandas import DataFrame as df
from sqlalchemy import create_engine
import psycopg2
from datetime import datetime

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from findmyhome.models.property import PropertyBuy, PropertyRent

map_type = {
  'for-sale': 'property_buy',
  'to-rent': 'property_rent',
}

def scrape_properties(action, province, city, region, code, page):
  price_upper = 2500000
  url = f'https://www.privateproperty.co.za/{action}/{province}/{city}/{region}/{code}?tp={price_upper}&page={page}'
  page = requests.get(url)
  soup = BeautifulSoup(page.text, features="lxml")
  results = soup.findAll('a',attrs={'class':'listingResult row'})
  properties = []
  
  for i in results:
    # Price
    raw_price = i.find(class_ = 'priceDescription').contents[0][2:].replace(" ", "")
    price = float(raw_price) if raw_price.isdigit() else None

    # Bedrooms
    bedroom_icon = i.find('div',attrs={'class':'icon bedroom'})
    bedroom_count = bedroom_icon.previous_sibling.previous_sibling.contents[0] if bedroom_icon != None else None

    # Bathrooms
    bathroom_icon = i.find('div',attrs={'class':'icon bathroom'})
    bathroom_count = bathroom_icon.previous_sibling.previous_sibling.contents[0] if bathroom_icon != None else None

    properties.append({
      'id': f"pp_{i.find(class_ = 'wishlistButton').attrs['data-listing-id']}",
      'title': i.attrs['title'],
      'price': price,
      'suburb': i.find(class_ = 'suburb').contents[0],
      'province': province,
      'city': city,
      'region': region,
      'bedroom_count': bedroom_count,
      'bathroom_count': bathroom_count,
      'href': i.attrs['href'],
      'created_at': datetime.now(),
      'updated_at': datetime.now(),
      'site': 'https://www.privateproperty.co.za/',
      'type': map_type[action],
    })
  return properties

# %%
page = 1
page_limit = 99999
price_upper = 2500000
end_flag = False
raw_data = []

while not end_flag:
  #result = scrape_properties('western-cape', 'cape-town', 'cape-town-city-bowl', '59', page)
  result = scrape_properties('for-sale', 'gauteng', 'pretoria', 'pretoria-east', '991', page)
  if len(result) > 0 and page < page_limit:
    PropertyBuy.bulk_upsert(result)
    page = page + 1
  else:
    end_flag = True
print("DONE")

# %%
page = 1
page_limit = 99999
price_upper = 2500000
end_flag = False
raw_data = []

while not end_flag:
  #result = scrape_properties('western-cape', 'cape-town', 'cape-town-city-bowl', '59', page)
  result = scrape_properties('to-rent', 'gauteng', 'pretoria', 'pretoria-east', '991', page)
  if len(result) > 0 and page < page_limit:
    PropertyRent.bulk_upsert(result)
    page = page + 1
  else:
    end_flag = True
print("DONE")

# %%
