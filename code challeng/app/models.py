from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin


db = SQLAlchemy()

class Restaurant (db.model, SerializerMixin):
    __tablename__ = 'restaurant'
    serialize_rules = ('-restaurant_pizzas')

    id = db.column(db.Interger,primary_key = True)
    name = db.column(db.String(250),nullable= False)
    address = db.Column(db.String(255), nullable=False)
    # lets make relationship
    Pizzas =db.relationship('RestaurantPizza', backref='restaurant')


class Pizza (db.model,SerializerMixin):

    __tablename__ ='pizza'
    serialize_rules = ('-pizza_restaurant')

    id = db.column(db.Interger,primary_key = True)
    name = db.column(db.String(250),nullable= False)
    ingredients = db.Column(db.String(255), nullable=False)
# making relationship

    Restaurants = db.relationship('RestaurantPizza', backref='pizza')


class RestaurantPizza (db.model,SerializerMixin):
    __tablename__=  'restaurant_pizaa'
    serialize_rules = ('-restaurant_pizzas','-pizza_restaurant')

    id = db.column(db.Interger,primary_key = True)
    price = db.Column(db.Decimal(10, 2), nullable=False)
    
    # making foreign key
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), primary_key=True)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), primary_key=True)

# adding validation rules

@validates('price')
def validate_price(self, key, price):
    if price < 1 or price > 30:
        raise ValueError('Price must be between 1 and 30')