# %%
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd

## Environmental variables
db_url = 'postgresql+psycopg2://juan:postgres@127.0.0.1/findmyhome' # TODO: Replace with environment variable
development = True

engine = create_engine(db_url, convert_unicode=True, echo=development)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

def init_db():
  Model.metadata.create_all(bind=engine)

Model = declarative_base(name="Model")
Model.query = db_session.query_property()

# %%
