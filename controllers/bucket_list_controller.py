from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models import City, Country, BucketList
from app import db

bucket_list_blueprint = Blueprint("bucket_list", __name__)



@bucket_list_blueprint.route("/my_list")
def get_form():
    cities = City.query.all()
    countries = Country.query.all()#These 2 lines GET all of the info from the db to allow the <select> tag to show all the options in the db
    bucket_list = BucketList.query.all()
    return render_template("/my_list/index.jinja", cities=cities, countries=countries, bucket_list=bucket_list)


@bucket_list_blueprint.route("/my_list",  methods=['POST'])
def add_to_list():
    visited = "visited" in request.form #trying to give visited a true or false value to determine which table it will be on(visited or no visited)
    name = request.form['city']
    bucket_list_item= BucketList(visited=visited, name=name)
    db.session.add(bucket_list_item)
    db.session.commit()
    return redirect('/my_list')


@bucket_list_blueprint.route('/my_list/<id>/toggle-visit', methods=['POST'])
def update_visited(id):
    item = BucketList.query.get(id)
    item.visited = not (item.visited)
    db.session.commit()
    return redirect('/my_list')

#.route(/my_list/add) when 'submit button is pressed

