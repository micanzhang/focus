__author__ = 'micanzhang'

from sqlalchemy import create_engine
import sqlalchemy.engine.url as url

host = 'localhost'
database = 'focus'
username = 'focus'
password = 'focus'

engine_url = url.URL(
    drivername='mysql+mysqldb',
    host=host,
    database=database,
    username=username,
    password=password,
)
engine = create_engine(engine_url, encoding='utf-8',convert_unicode=True)