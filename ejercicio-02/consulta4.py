from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_

from genera_base import Country 

engine = create_engine('sqlite:///basecountries.db')

Session = sessionmaker(bind=engine)
session = Session()

#Presentar los países ordenados por la capital, siempre que el país pertenezca a Europa
consulta = session.query(Country).filter(Country.continente=="EU").order_by(Country.capital).all()
print(consulta)