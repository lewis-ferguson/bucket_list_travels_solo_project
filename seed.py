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
    city1 = City(name="Edinburgh")
    city2 = City(name="Glasgow")
    city3 = City(name="London")
    country1 = Country(name="Scotland")
    country2 = Country(name="England")

    db.session.add(city1)
    db.session.add(city2)
    db.session.add(city3)

    db.session.add(country1)
    db.session.add(country2)
    db.session.commit()