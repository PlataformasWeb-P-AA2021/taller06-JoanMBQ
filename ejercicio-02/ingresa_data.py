from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_base import Country

import requests

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///basecountries.db')

Session = sessionmaker(bind=engine)
session = Session()


data = requests.get('https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json')

datos_json = data.json()

for d in datos_json:
    p = Country(
        nombre = d['CLDR display name'],
        capital = d['Capital'],
        continente = d['Continent'],
        dial= d['Dial'],
        geonameID = d['Geoname ID'],
        itu = d['ITU'],
        lenguajes = d['Languages'],
        independiente =d['is_independent'])
    session.add(p)

session.commit()

