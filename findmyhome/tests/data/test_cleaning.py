
from findmyhome.data.cleaning import std_method, iqr_method, pct_method, is_outlier

import pandas as pd
import numpy as np
import pytest

data_records = np.array([(0,  'pp_3578951', '2020-10-28T10:51:31.321391000', '2020-10-28T11:14:40.437434000', '3 Bed Townhouse in Wapadrand',  9500.,  'Wapadrand', 3., 2. , '/to-rent/gauteng/pretoria/pretoria-east/wapadrand/23-burkea-park/930-buikgord-street/RR1331655',   'https://www.privateproperty.co.za/', 'gauteng', 'pretoria', 'pretoria-east', 'property_rent'),
                         (1,  'pp_7138809', '2020-10-28T10:51:31.322542000', '2020-10-28T11:14:40.437989000', '2 Bed Apartment in Boardwalk',  7500.,  'Boardwalk', 2., 1. , '/to-rent/gauteng/pretoria/pretoria-east/boardwalk/RR2877176',                                      'https://www.privateproperty.co.za/', 'gauteng', 'pretoria', 'pretoria-east', 'property_rent'),
                         (2,  'pp_7108705', '2020-10-28T10:51:31.323097000', '2020-10-28T11:14:40.438548000', '2 Bed Duplex in Olympus AH',    8500.,  'Olympus',   2., 1. , '/to-rent/gauteng/pretoria/pretoria-east/olympus/55-lavender-close/1-sunrise-road/RR2864334',       'https://www.privateproperty.co.za/', 'gauteng', 'pretoria', 'pretoria-east', 'property_rent'),
                         (3,  'pp_4011017', '2020-10-28T11:15:37.449035000', '2020-10-28T11:15:37.449036000', '3 Bed Apartment in Equestria',  10400., 'Equestria', 3., 2. , '/to-rent/gauteng/pretoria/pretoria-east/equestria/14-sh-mac/202-stellenberg-road/RR1497939',       'https://www.privateproperty.co.za/', 'gauteng', 'pretoria', 'pretoria-east', 'property_rent'),
                         (4,  'pp_4010916', '2020-10-28T11:15:37.449516000', '2020-10-28T11:15:37.449518000', '3 Bed Duplex in Equestria',     9000.,  'Equestria', 3., 2.5, '/to-rent/gauteng/pretoria/pretoria-east/equestria/45-peters-place/790-stellenberg-road/RR1497893', 'https://www.privateproperty.co.za/', 'gauteng', 'pretoria', 'pretoria-east', 'property_rent'),
                         (5,  'pp_3837583', '2020-10-28T11:15:37.449960000', '2020-10-28T11:15:37.449961000', '3 Bed Apartment in Equestria',  9900.,  'Equestria', 3., 2. , '/to-rent/gauteng/pretoria/pretoria-east/equestria/26-megan-lee/202-stellenberg-road/RR1428365',    'https://www.privateproperty.co.za/', 'gauteng', 'pretoria', 'pretoria-east', 'property_rent'),
                         (6,  'pp_7108705', '2020-10-28T10:51:31.323097000', '2020-10-28T11:14:40.438548000', '2 Bed Duplex in Olympus AH',    8500.,  'Olympus',   2., 1. , '/to-rent/gauteng/pretoria/pretoria-east/olympus/55-lavender-close/1-sunrise-road/RR2864334',       'https://www.privateproperty.co.za/', 'gauteng', 'pretoria', 'pretoria-east', 'property_rent'),
                         (7,  'pp_7108705', '2020-10-28T10:51:31.323097000', '2020-10-28T11:14:40.438548000', '2 Bed Duplex in Olympus AH',    8500.,  'Olympus',   2., 1. , '/to-rent/gauteng/pretoria/pretoria-east/olympus/55-lavender-close/1-sunrise-road/RR2864334',       'https://www.privateproperty.co.za/', 'gauteng', 'pretoria', 'pretoria-east', 'property_rent'),
                         (8,  'pp_7108705', '2020-10-28T10:51:31.323097000', '2020-10-28T11:14:40.438548000', '2 Bed Duplex in Olympus AH',    8500.,  'Olympus',   2., 1. , '/to-rent/gauteng/pretoria/pretoria-east/olympus/55-lavender-close/1-sunrise-road/RR2864334',       'https://www.privateproperty.co.za/', 'gauteng', 'pretoria', 'pretoria-east', 'property_rent'),
                         (9,  'pp_7108705', '2020-10-28T10:51:31.323097000', '2020-10-28T11:14:40.438548000', '2 Bed Duplex in Olympus AH',    8500.,  'Olympus',   2., 1. , '/to-rent/gauteng/pretoria/pretoria-east/olympus/55-lavender-close/1-sunrise-road/RR2864334',       'https://www.privateproperty.co.za/', 'gauteng', 'pretoria', 'pretoria-east', 'property_rent'),
                         (10, 'pp_7108705', '2020-10-28T10:51:31.323097000', '2020-10-28T11:14:40.438548000', '2 Bed Duplex in Olympus AH',    8500.,  'Olympus',   2., 1. , '/to-rent/gauteng/pretoria/pretoria-east/olympus/55-lavender-close/1-sunrise-road/RR2864334',       'https://www.privateproperty.co.za/', 'gauteng', 'pretoria', 'pretoria-east', 'property_rent'),
                         (11, 'pp_7108705', '2020-10-28T10:51:31.323097000', '2020-10-28T11:14:40.438548000', '2 Bed Duplex in Olympus AH',    8500.,  'Olympus',   2., 1. , '/to-rent/gauteng/pretoria/pretoria-east/olympus/55-lavender-close/1-sunrise-road/RR2864334',       'https://www.privateproperty.co.za/', 'gauteng', 'pretoria', 'pretoria-east', 'property_rent'),
                         (12, 'pp_7108705', '2020-10-28T10:51:31.323097000', '2020-10-28T11:14:40.438548000', '2 Bed Duplex in Olympus AH',    8500.,  'Olympus',   2., 1. , '/to-rent/gauteng/pretoria/pretoria-east/olympus/55-lavender-close/1-sunrise-road/RR2864334',       'https://www.privateproperty.co.za/', 'gauteng', 'pretoria', 'pretoria-east', 'property_rent'),
                         (13, 'pp_7108705', '2020-10-28T10:51:31.323097000', '2020-10-28T11:14:40.438548000', '2 Bed Duplex in Olympus AH',    8500.,  'Olympus',   2., 1. , '/to-rent/gauteng/pretoria/pretoria-east/olympus/55-lavender-close/1-sunrise-road/RR2864334',       'https://www.privateproperty.co.za/', 'gauteng', 'pretoria', 'pretoria-east', 'property_rent'),
                         (14, 'pp_7108705', '2020-10-28T10:51:31.323097000', '2020-10-28T11:14:40.438548000', '2 Bed Duplex in Olympus AH',    8500.,  'Olympus',   2., 1. , '/to-rent/gauteng/pretoria/pretoria-east/olympus/55-lavender-close/1-sunrise-road/RR2864334',       'https://www.privateproperty.co.za/', 'gauteng', 'pretoria', 'pretoria-east', 'property_rent'),
                         (15, 'pp_7108705', '2020-10-28T10:51:31.323097000', '2020-10-28T11:14:40.438548000', '2 Bed Duplex in Olympus AH',    8500.,  'Olympus',   2., 1. , '/to-rent/gauteng/pretoria/pretoria-east/olympus/55-lavender-close/1-sunrise-road/RR2864334',       'https://www.privateproperty.co.za/', 'gauteng', 'pretoria', 'pretoria-east', 'property_rent'),
                         (16, 'pp_7108705', '2020-10-28T10:51:31.323097000', '2020-10-28T11:14:40.438548000', '2 Bed Duplex in Olympus AH',    8500.,  'Olympus',   2., 1. , '/to-rent/gauteng/pretoria/pretoria-east/olympus/55-lavender-close/1-sunrise-road/RR2864334',       'https://www.privateproperty.co.za/', 'gauteng', 'pretoria', 'pretoria-east', 'property_rent'),
                         (17, 'pp_3837583', '2020-10-28T11:15:37.449960000', '2020-10-28T11:15:37.449961000', 'This is bad data',              9900.,  'Equestria', 10, 2. , '/to-rent/gauteng/pretoria/pretoria-east/equestria/26-megan-lee/202-stellenberg-road/RR1428365',    'https://www.privateproperty.co.za/', 'gauteng', 'pretoria', 'pretoria-east', 'property_rent')],
 dtype=[('index', '<i8'), ('id', 'O'), ('created_at', '<M8[ns]'), ('updated_at', '<M8[ns]'), ('title', 'O'), ('price', '<f8'), ('suburb', 'O'), ('bedroom_count', '<f8'), ('bathroom_count', '<f8'), ('href', 'O'), ('site', 'O'), ('province', 'O'), ('city', 'O'), ('region', 'O'), ('type', 'O')])
data = pd.DataFrame.from_records(data_records)

def test_iqr_method():
  result = iqr_method(data)

  # Test min and max price
  assert result[0]['price'] == 7937.5
  assert result[1]['price'] == 9437.5
  
  # Test min and max bedroom counts
  assert result[0]['bedroom_count'] == 0.875
  assert result[1]['bedroom_count'] == 3.875
  
  # Test min and max bathroom counts
  assert result[0]['bathroom_count'] == -0.125
  assert result[1]['bathroom_count'] == 2.875


def test_std_method():
  result = std_method(data)
  
  # Test min and max price
  assert result[0]['price'] == 6754.4629529332715
  assert result[1]['price'] == 10823.314824844507
  
  # Test min and max bedroom counts
  assert result[0]['bedroom_count'] == -2.8105589083849947
  assert result[1]['bedroom_count'] == 8.143892241718328
  
  # Test min and max bathroom counts
  assert result[0]['bathroom_count'] == -0.20597420671253208
  assert result[1]['bathroom_count'] == 2.8170853178236435

def test_pct_method():
  level = 1
  result = pct_method(data, level)

  # Test min and max price
  assert result[0]['price'] == 7670.0
  assert result[1]['price'] == 10314.999999999998
  
  # Test min and max bedroom counts
  assert result[0]['bedroom_count'] == 2.0
  assert result[1]['bedroom_count'] == 8.809999999999988
  
  # Test min and max bathroom counts
  assert result[0]['bathroom_count'] == 1.0
  assert result[1]['bathroom_count'] == 2.414999999999999

def test_is_outlier():
  result = is_outlier(data['bedroom_count'])

  assert result.where(result == False).count() == 1
