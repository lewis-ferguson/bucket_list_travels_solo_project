from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models import City, Country, BucketList
from app import db

bucket_list_blueprint = Blueprint("bucket_list", __name__)



@bucket_list_blueprint.route("/my_list")
def get_form():
    cities = City.query.all()
    countries = Country.query.all()
    bucket_list = BucketList.query.all()
    return render_template("/my_list/index.jinja", cities=cities, countries=countries, bucket_list=bucket_list)


@bucket_list_blueprint.route("/my_list",  methods=['POST'])
def add_to_list():
    visited= request.form['visited']
    city_id = request.form['city_name']#testing out using city_name instead of city_id
    bucket_list_item= BucketList(visited=visited, city_id=city_id)
    db.session.add(bucket_list_item)
    db.session.commit()
    return redirect('/my_list')

