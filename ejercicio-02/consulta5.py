from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_

from genera_base import Country 

engine = create_engine('sqlite:///basecountries.db')

Session = sessionmaker(bind=engine)
session = Session()

#Presentar todos los países que tengan en su cadena de nombre de país "uador" o en su cadena de capital "ito".
consulta = session.query(Country).filter(or_(Country.nombre.like("%uador%"), Country.capital.like("%ito%"))).all() 
print(consulta)
