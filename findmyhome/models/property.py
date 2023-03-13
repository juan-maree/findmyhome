# %%
from findmyhome.data.cleaning import std_method
from findmyhome.db.database import Model, db_session, engine

from sqlalchemy import Column, String, DateTime, Float, ForeignKey
from sqlalchemy.dialects import postgresql
import pandas as pd

class Property(Model):
  __tablename__ = 'property'
  id = Column(String, primary_key=True)
  created_at = Column(DateTime)
  updated_at = Column(DateTime)
  title = Column(String)
  price = Column(Float)
  suburb = Column(String)
  bedroom_count = Column(Float)
  bathroom_count = Column(Float)
  href = Column(String)
  site = Column(String)
  province = Column(String)
  city = Column(String)
  region = Column(String)
  type = Column(String(50))

  __mapper_args__ = {
      'polymorphic_identity':'property',
      'polymorphic_on':type
  }

  def __repr__(self):
    return f"<'{self.__table__}'(ID='{self.id}', title='{self.title}')>"

  @classmethod
  def to_df(cls):
    return pd.read_sql_table(Property.__tablename__, con=engine)

  @classmethod
  def get_data(cls):
    data = cls.to_df()
    return data[data['type'] == cls.__tablename__]

  @classmethod
  def bulk_upsert(cls, data):
    session = db_session()

    try:
      insert_statement = postgresql.insert(Property.__table__) # Move this to DB

      #insert_statement = postgresql.insert(cls.__table__)
      update_columns = {col.name: col for col in insert_statement.excluded if col.name not in ('id', 'created_at')}
      session.execute(
        insert_statement
        .values(data)
        .on_conflict_do_update(
          index_elements=[cls.id],
          set_ = update_columns
        )
      )
      session.commit()
    except:
      session.rollback()
      raise
    finally:
      session.close()

class PropertyBuy(Property):
  __tablename__ = 'property_buy'
  id = Column(String, ForeignKey('property.id'), primary_key=True)

  __mapper_args__ = {
      'polymorphic_identity':'property_buy',
  }

class PropertyRent(Property):
  __tablename__ = 'property_rent'
  id = Column(String, ForeignKey('property.id'), primary_key=True)

  __mapper_args__ = {
      'polymorphic_identity':'property_rent',
  }
