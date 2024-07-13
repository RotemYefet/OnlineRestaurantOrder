from app import app 
from models import Client
from menu_db_handler import itemHandler
from order_db_handler import orderHandler
from client_db_handler import clientHandler
from flask import request, jsonify, make_response
from werkzeug.security import generate_password_hash
import sqlite3
from flask import make_response, jsonify, request
from flask_restful import Resource
from werkzeug.security import check_password_hash


class Home(Resource):
    def get(self):
        return {"message": "Welcome to Home"}

class About(Resource):
    def get(self):
        return {"message": "About Us"}

class Menu(Resource):
    def get(self):
        return {"message": "Our Menu"}

class Payment(Resource):
    def get(self):
        return {"message": "Payment Page"}

class AuthComponent(Resource):
    def get(self):
        return {"message": "Authentication Page"}

def initialize_routes(api):
    api.add_resource(Home, '/Home')
    api.add_resource(About, '/About')
    api.add_resource(Menu, '/Menu')
    api.add_resource(Payment, '/Payment')
    api.add_resource(AuthComponent, '/AuthComponent')

@app.route('/api/allMenuItems', methods=['GET'])
def getAllMenuItems():
    ## FROM DB ##

    ## Get all items from the db
    all_items = itemHandler.getAllItemsDB(0)
    # make a list to return
    list = convert_db_item_to_list(all_items)
    # create a http response
    response = make_response(jsonify({'menu items': list}), 200)


    ## LOCAL DATA ##
    # list = {
    #     'item_name': "pasta",
    #     'item_type': "food",
    #     'item_price': "20$"
    # }
    # # RESPONSE (WHAT YOU SENT TO FRONEND)
    # response = make_response(jsonify({'menu items': list}), 200)
    return response


@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('user_name')
    password = data.get('password')

    # Checking If Username Or Password Is Empty
    if not username or not password:
        return make_response(jsonify({'error': 'Username and password are required'}), 400)

    # Check if user already exists in the database
    conn = sqlite3.connect('instance/db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Client WHERE user_name = ?", (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        conn.close()
        return make_response(jsonify({'error': 'Username already exists'}), 409)

    # Add user to the database
    cursor.execute("INSERT INTO Client (user_name, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

    return make_response(jsonify({'message': 'User created successfully'}), 201)


@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('user_name')
    password = data.get('password')

    if not username or not password:
        return make_response(jsonify({'error': 'Username and password are required'}), 400)

    # Check user in the database
    conn = sqlite3.connect('instance/db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Client WHERE user_name = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    # Checking If Username Password Is Currect
    if user and user[2] == password:  # Assuming password is the third column
        return make_response(jsonify({'message': 'Login successful'}), 200)
    else:
        return make_response(jsonify({'error': 'Invalid username or password'}), 401)

@app.route('/api/users', methods=['GET'])
def get_users():
    conn = sqlite3.connect('instance/db.sqlite3')
    conn.row_factory = sqlite3.Row  # This allows us to access the rows as dictionaries
    cursor = conn.cursor()

    cursor.execute("SELECT user_name FROM Client")
    rows = cursor.fetchall()
    conn.close()

    users = [dict(row) for row in rows]

    return jsonify({'users': users})


def convert_db_item_to_list(items):
        list = []
        for item in items:
            list.append({
                'item_name': item.item_name,
                'item_type': item.item_type,
                'item_price': item.item_price
            })
        return list



# @app.route('/api/createOrder', methods=['POST'])
# def createOrder():
#     ##get the data from the request
#     order_data = request.get_json()
#     ## send the data to db (create the row)
#     order_created = orderHandler.createOrderDB(order_data)

#     ## check that "order review" and "order rate" are not null. If there null, write a message
#     if order_created.order_review is not None:
#         order_review = order_created.order_review
#     else:
#         order_review = "no order review"

#     if order_created.order_rate is not None:
#         order_rate = order_created.order_rate
#     else:
#         order_rate = "no order review"

#     return("Order created on DB-" + "\n" +
#             "client_id: " + order_created.client_id + "\n" +
#             "order products: " + order_created.order_products + "\n" + 
#             "order price: " + order_created.order_price + "\n" + 
#             "order status: " + order_created.order_status + "\n" +
#             "order review: " + order_review + "\n" +
#             "order rate: " + order_rate + "\n"
#             )

@app.route('/api/createOrder', methods=['POST'])
def create_order():
    data = request.get_json()
    client_id = data.get('client_id')
    order_products = data.get('order_products')
    order_price = data.get('order_price')
    order_status = data.get('order_status', 'pending')
    order_review = data.get('order_review', '')
    order_rate = data.get('order_rate', '')

    if not client_id or not order_products or not order_price:
        return make_response(jsonify({'error': 'Missing required fields'}), 400)

    conn = sqlite3.connect('instance/db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO "Order" (client_id, order_products, order_price, order_status, order_review, order_rate) VALUES (?, ?, ?, ?, ?, ?)',
                   (client_id, order_products, order_price, order_status, order_review, order_rate))
    conn.commit()
    conn.close()

    return make_response(jsonify({'message': 'Order created successfully'}), 201)


