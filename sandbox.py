from database import PropertyBuy
# %%
data = PropertyBuy.to_df()
unpriced = data[data['price'].isna()]
priced = data.dropna(subset=['price'])

# %%
plot_data = priced

# %%
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

sns.jointplot(x='bedroom_count', y='price', data=plot_data)
plt.show()

# %%
fig, ax =plt.subplots(3,1, figsize=(12,20))
sns.countplot(plot_data['bedroom_count'], ax=ax[0])
sns.countplot(plot_data['bedroom_count'], ax=ax[1])
sns.countplot(plot_data['suburb'], ax=ax[2])
ax[2].set_xticklabels(ax[2].get_xticklabels(), rotation=50, ha="right")
plt.show()

# %%
alchemyEngine = create_engine('postgresql+psycopg2://juan:postgres@127.0.0.1/findmyhome', pool_recycle=3600)
postgreSQLConnection = alchemyEngine.connect()
postgreSQLTable = "properties_buy"

try:
  frame = data.to_sql(postgreSQLTable, postgreSQLConnection, index_label='id', if_exists='append')
except ValueError as vx:
    print(vx)
except Exception as ex:  
    print(ex)
else:
  print("PostgreSQL Table %s has been created successfully." % postgreSQLTable)
finally:
  postgreSQLConnection.close()


# %%
from sqlalchemy.dialects import postgresql

data = [{'id': 'pp_7025618',
  'title': '2 Bed House in Olympus AH',
  'price': 6800.0,
  'suburb': 'Olympus',
  'province': 'gauteng',
  'city': 'pretoria',
  'region': 'pretoria-east',
  'bedroom_count': '2',
  'bathroom_count': '1',
  'href': '/to-rent/gauteng/pretoria/pretoria-east/olympus/16-the-courts/45-neptune-street/RR2827364',
  'created_at': datetime.datetime(2020, 10, 28, 10, 21, 51, 27927),
  'updated_at': datetime.datetime(2020, 10, 28, 10, 21, 51, 27928),
  'site': 'https://www.privateproperty.co.za/',
  'type': 'property_rent'},
 {'id': 'pp_5973652',
  'title': '2 Bed Flat in Lynnwood Manor',
  'price': 7700.0,
  'suburb': 'Lynnwood Manor',
  'province': 'gauteng',
  'city': 'pretoria',
  'region': 'pretoria-east',
  'bedroom_count': '2',
  'bathroom_count': '1.5',
  'href': '/to-rent/gauteng/pretoria/pretoria-east/lynnwood-manor/5-cambray/27-ringwood-road/RR2355485',
  'created_at': datetime.datetime(2020, 10, 28, 10, 21, 51, 28496),
  'updated_at': datetime.datetime(2020, 10, 28, 10, 21, 51, 28497),
  'site': 'https://www.privateproperty.co.za/',
  'type': 'property_rent'}]
