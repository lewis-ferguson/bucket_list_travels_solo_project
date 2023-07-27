from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models import City, Country, BucketListCities
from app import db

destinations_blueprint = Blueprint("destinations", __name__)

@destinations_blueprint.route("/destinations")
def destinations():
    cities = City.query.all()
    countries = Country.query.all()
    return render_template("/destinations/index.jinja", cities = cities, countries = countries)