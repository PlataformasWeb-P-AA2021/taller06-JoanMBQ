from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_

from genera_base import Country 

engine = create_engine('sqlite:///basecountries.db')

Session = sessionmaker(bind=engine)
session = Session()

#Presentar todos los países del continente americano
consulta = session.query(Country).filter(Country.continente=="NA").all()
print(consulta)