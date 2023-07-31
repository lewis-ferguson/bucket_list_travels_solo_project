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

@destinations_blueprint.route('/destinations/<id>')#show individual country
def show_country(id):
    chosen_country = Country.query.get(id)
    return render_template('/destinations/show.jinja', title="Destination" ,country = chosen_country)


@destinations_blueprint.route('/destinations/<id>', methods=['POST'])
def edit_country(id): #Post method to update country
    new_name = request.form['country']
    chosen_country = Country.query.get(id)
    chosen_country.name = new_name
    db.session.commit()
    return redirect('/destinations')

# @destinations.route('/destinations/<city_id>/delete', methods=['POST'])
# def delete(city_id):
#   remove_city(city_id)
#   return redirect('/destinations')  #remove a city