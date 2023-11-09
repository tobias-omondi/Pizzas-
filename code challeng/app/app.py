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

@app.route('/restaurants', methods =['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    json_restaurants = []
    for restaurant in restaurants:
        json_restaurant = [{
            'id':restaurant.id,
            'name':restaurant.name,
            'address':restaurant.address
        }]
        json_restaurants.append(json_restaurant)
        response = make_response(
            jsonify(json_restaurants),200
        )
    
    return response

@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant_by_id(id):
    restaurant = Restaurant.query.get(id)
    
    if restaurant:
        restaurant_json = {
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address
            
        }
        
        return jsonify(restaurant_json), 200
    
    
    return jsonify({'error': 'Restaurant not found'}), 404

@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    
    if restaurant:
        RestaurantPizza.query.filter_by(restaurant_id=id).delete()
        
        # Delete the Restaura..
        db.session.delete(restaurant)
        db.session.commit()
        
        # emty response returned
        return '', 204
    
    return jsonify({'error': 'Restaurant not found'}), 404

@app.route("/pizzas",methods = ['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    json_pizzas = []
    for pizza in pizzas:
        json_pizza = {
            'id': pizza.id,
            'name': pizza.name,
            'ingredient': pizza.ingredients,  
        }
        json_pizzas.append(json_pizza)
    resp = make_response(jsonify(json_pizzas), 200)
    return resp

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    try:
        data = request.get_json()
        price = data.get('price')
        pizza_id = data.get('pizza_id')
        restaurant_id = data.get('restaurant_id')
        
        pizza = Pizza.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)
        
        if pizza is None or restaurant is None:
            response = {
                "errors": ["Pizza or restaurant not found"]
            }
            return jsonify(response), 404
        
        new_restaurant_pizza = RestaurantPizza(
            price=price,
            pizza_id=pizza_id,
            restaurant_id=restaurant_id
        )
        
        db.session.add(new_restaurant_pizza)
        db.session.commit()
        
        response_data = {
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        }
        
        return jsonify(response_data), 201 
    except Exception as e:
        response = {
            "errors": ["Validation errors"]
        }
        return jsonify(response), 400

if __name__ == '__main__':
    app.run(port=5552, debug= True)