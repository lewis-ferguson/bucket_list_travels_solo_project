from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user@localhost:5432/bucket_list"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from seed import seed
app.cli.add_command(seed)

# from controllers.city_controller import cities_blueprint
# from controllers.country_controller import countries_blueprint
from controllers.destinations_controller import destinations_blueprint


app.register_blueprint(destinations_blueprint)
# app.register_blueprint(countries_blueprint)


@app.route('/')
def home():
    return render_template('index.jinja')

if __name__ == '__main__':
    app.run(debug=True)