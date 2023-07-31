from app import db
from models import City, Country, BucketList
import click

from flask.cli import with_appcontext

@click.command(name='seed')
@with_appcontext
def seed():
    City.query.delete()
    Country.query.delete()
    BucketList.query.delete()
    
    country1 = Country(name="Scotland")
    country2 = Country(name="England")
    country3 = Country(name="Turkey")
    country4 = Country(name="Thailand")
    db.session.add(country1)
    db.session.add(country2)
    db.session.add(country3)
    db.session.add(country4)
    db.session.commit()
    
    city1 = City(name="Edinburgh", country_id = country1.id)
    city2 = City(name="Glasgow", country_id = country1.id)
    city3 = City(name="London",country_id = country2.id)
    city4 = City(name="Dalaman",country_id = country3.id)
    city5 = City(name="Bangkok", country_id = country4.id)
    city6 = City(name="Phuket" , country_id = country4.id)
    city7 = City(name="Antalya", country_id = country3.id)
    city8 = City(name="Manchester", country_id = country2.id)

    db.session.add(city1)
    db.session.add(city2)
    db.session.add(city3)
    db.session.add(city4)
    db.session.add(city5)
    db.session.add(city6)
    db.session.add(city7)
    db.session.add(city8)

 
    db.session.commit()