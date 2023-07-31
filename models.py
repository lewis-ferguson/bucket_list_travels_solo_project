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

    
    
class BucketList(db.Model):
    __tablename__='bucket_list'
    
    id = db.Column(db.Integer, primary_key= True)
    visited = db.Column(db.Boolean)
    name = db.Column(db.String(64)) #testing
    city_id = db.ForeignKey('cities_id')
        