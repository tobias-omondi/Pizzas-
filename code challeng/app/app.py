# Routes
from flask import Flask, make_response,jsonify,request
from flask_migrate import Migrate
from flask_restful import Api,Resource

from models import db, Pizza, Restaurant, RestaurantPizza 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)
api = Api(app)

class Home(Resource):
    def get(self):
        response_dict = {
            "message": "Welcome to the Best Offers Pizza"
        }
        response = make_response(
            jsonify(response_dict),200,
        )
        return response
api.add_resource(Home, "/")


if __name__ == '__main__':
    app.run(port=5552, debug= True)