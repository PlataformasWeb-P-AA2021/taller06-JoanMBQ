from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_

from genera_base import Country 

engine = create_engine('sqlite:///basecountries.db')

Session = sessionmaker(bind=engine)
session = Session()

countries = session.query(Country).all()

#Presentar los lenguajes de cada país.
for p in countries:
    print("Pais: %-30sLenguajes:%s" % (p.nombre, p.lenguajes))
    print("--------------------------------------------------------------------------")