from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models import City, Country, BucketList
from app import db

destinations_blueprint = Blueprint("destinations", __name__)

@destinations_blueprint.route("/destinations")#gets all the countries and cities
def destinations():
    cities = City.query.all()
    countries = Country.query.all()
    return render_template("/destinations/index.jinja", cities = cities, countries = countries)


@destinations_blueprint.route("/destinations",  methods=['POST'])
def add_country():#add a country
    country_name = request.form['country']
    new_country = Country(name = country_name)
    db.session.add(new_country)
    db.session.commit()
    return redirect('/destinations')

@destinations_blueprint.route('/destinations/<country_name>')#show individual country
def show_country(country_name):
    chosen_country = Country.query.filter(Country.name.ilike(country_name)).first()
    return render_template('/destinations/show.jinja', title="Destination" ,country = chosen_country)


@destinations_blueprint.route('/destinations/<id>', methods=['POST'])
def edit_country(id): #Post method to update country
    new_name = request.form['country']
    chosen_country = Country.query.get(id)
    chosen_country.name = new_name
    db.session.commit()
    return redirect('/destinations')

@destinations_blueprint.route("/destinations/<id>/add-city",  methods=['POST'])
def add_city(id):#add a city to a country
    country = Country.query.get(id)
    city_name = request.form['city']
    country_id = country.id
    new_city = City(name = city_name, country_id = country_id)
    db.session.add(new_city)
    db.session.commit()
    return redirect('/destinations')

@destinations_blueprint.route('/destinations/<city_id>/delete', methods=['POST'])
def delete(city_id):#deletes a city
    city = City.query.get(city_id)
    db.session.delete(city)
    db.session.commit()
    return redirect('/destinations')  #remove a city

@destinations_blueprint.route('/destinations/search', methods=['POST'])
def search():#show a country by search
    country_name = request.form['search_country']
    # country = Country.query.filter_by(name=country_name).first()
    return redirect(f'/destinations/{country_name}')
    