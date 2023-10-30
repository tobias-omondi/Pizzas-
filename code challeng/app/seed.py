#!/usr/bin/env python3

from app import app, db
from models import Restaurant, Pizza, RestaurantPizza

def seed_data():
    with app.app_context():
        try:
            # Deleting existing data
            RestaurantPizza.query.delete()
            Pizza.query.delete()
            Restaurant.query.delete()

            # Seeding restaurants
            restaurant_data = [
                {"name": "BIG moutain", "address": "9900fg33"},
                {"name": "Colrado", "address": "gh33894 B"},
                {"name": "Chiken in", "address": "29044-- C"},
                {"name": "Bardgers", "address": "29uut044--"},
                {"name": "Chiken legit", "address": "3943344-- C"},
                {"name": "OGkings", "address": "world 22339-- C"},
                {"name": "GIGchy", "address": "28844-- C"},
                {"name": "Pizza Palace", "address": "1234 Elm Street"},
                {"name": "Sushi Delight", "address": "567 Sushi Lane"},
                {"name": "Mediterranean Grill", "address": "789 Olive Avenue"}
            ]
               

            for data in restaurant_data:
                restaurant = Restaurant(name=data["name"], address=data["address"])
                db.session.add(restaurant)

            db.session.commit()
            print("🍽️ Seeded restaurants...")

            # Seeding pizzas
            pizza_data = [
               {"name": "Pizza Margherita Extra Cheese", "ingredients": "Tomato, Mozzarella, Basil, Extra Cheese"},
               {"name": "Pizza Four Seasons", "ingredients": "Tomato, Mozzarella, Ham, Artichokes, Mushrooms, Olives"},
               {"name": "Pizza White Garlic", "ingredients": "White Garlic Sauce, Mozzarella, Chicken, Spinach, Sun-Dried Tomatoes"},
               {"name": "Pizza Pesto Delight", "ingredients": "Pesto Sauce, Mozzarella, Cherry Tomatoes, Fresh Basil, Pine Nuts"},
               {"name": "Pizza Spinach and Feta", "ingredients": "Tomato, Mozzarella, Spinach, Feta Cheese, Garlic, Olive Oil"},
               {"name": "Pizza Buffalo Chicken", "ingredients": "Buffalo Sauce, Mozzarella, Chicken, Red Onions, Blue Cheese"},
               {"name": "Pizza BBQ Bacon Ranch", "ingredients": "BBQ Sauce, Mozzarella, Bacon, Red Onions, Ranch Drizzle"},
               {"name": "Pizza Veggie Supreme", "ingredients": "Tomato, Mozzarella, Mushrooms, Bell Peppers, Onions, Black Olives"},
               {"name": "Pizza Mediterranean Delight", "ingredients": "Tomato, Mozzarella, Kalamata Olives, Red Onions, Feta, Tzatziki Drizzle"},
               {"name": "Pizza Shrimp Scampi", "ingredients": "White Wine Garlic Butter Sauce, Mozzarella, Shrimp, Garlic, Parsley"}
            ]
            for data in pizza_data:
                pizza = Pizza(name=data["name"], ingredients=data["ingredients"])
                db.session.add(pizza)

            db.session.commit()
            print("🍕 Seeded pizzas...")

            # Adding restaurant-pizza associations
            restaurant_pizza_data = [
               {"restaurant_id": 2, "pizza_id": 4, "price": 14.99},
               {"restaurant_id": 3, "pizza_id": 1, "price": 11.99},
               {"restaurant_id": 4, "pizza_id": 6, "price": 16.99},
               {"restaurant_id": 5, "pizza_id": 8, "price": 15.99},
               {"restaurant_id": 6, "pizza_id": 9, "price": 12.99},
               {"restaurant_id": 7, "pizza_id": 3, "price": 13.99},
               {"restaurant_id": 8, "pizza_id": 7, "price": 14.99},
               {"restaurant_id": 9, "pizza_id": 5, "price": 17.99},
               {"restaurant_id": 10, "pizza_id": 2, "price": 12.99},
               {"restaurant_id": 1, "pizza_id": 10, "price": 15.99}
            ]

            for data in restaurant_pizza_data:
                association = RestaurantPizza(
                    restaurant_id=data["restaurant_id"],
                    pizza_id=data["pizza_id"],
                    price=data["price"]
                )
                db.session.add(association)

            db.session.commit()
            print("🍽️🍕 Added restaurant-pizza ...")

            print("🍽️🍕🍽️ Done seeding!")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    seed_data()
