from sqlalchemy import create_engine

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///basecountries.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Country(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    capital = Column(String)
    continente = Column(String)
    dial = Column(String)
    geonameID = Column(String)
    itu = Column(String)
    lenguajes = Column(String)
    independiente = Column(String)
    
    def __repr__(self):
        return "Country: nombre=%s capital=%s continente:%s dial:%s geonameID:%s itu:%s lenguajes:%s independiente:%s \n" % (
				self.nombre, 
				self.capital, 
				self.continente,
				self.dial,
				self.geonameID,
				self.itu,
				self.lenguajes,
				self.independiente)

Base.metadata.create_all(engine)
