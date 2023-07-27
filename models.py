from app import db

class Country(db.Model):
    __tablename__="countries"
    
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(64))
    cities = db.relationship('City', backref='Country')


class City(db.Model):
    __tablename__="cities"
    
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64))
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id') )

    
    
class BucketListCities(db.Model):
    __tablename__='bucket_list_cities'
    
    id = db.Column(db.Integer, primary_key= True)
    visited = db.Column(db.Boolean)
    city_id = db.ForeignKey('cities_id')
        