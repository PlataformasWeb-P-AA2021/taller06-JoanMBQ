from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_

from genera_base import Country 

engine = create_engine('sqlite:///basecountries.db')

Session = sessionmaker(bind=engine)
session = Session()

#Presentar los países de Asía, ordenados por el atributo Dial.
consulta = session.query(Country).filter(Country.continente=="AS").order_by(Country.dial).all()
print(consulta)