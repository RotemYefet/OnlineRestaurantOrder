from flask import Flask, request, jsonify 
from flask_cors import CORS
from order_db_handler import orderHandler
from client_db_handler import clientHandler
from menu_db_handler import itemHandler
app = Flask(__name__)
CORS= CORS(app, origins="*") #אבטחה

### CLIENTS ###

## Get client from db by id##
client_by_id = clientHandler.getClientDB(1)
print(client_by_id.user_name + " " + client_by_id.password + "\n")

## Get all clients from db ##
all_clients = clientHandler.getAllClientsDB(0)
for client in all_clients:
    print(client.user_name + " " + client.password + "\n")

## Delete client from db by id##
client_deleted_by_id = clientHandler.deleteClientDB(1)
print(client_deleted_by_id.user_name + " " + client_deleted_by_id.password + " " + "was deleted from db" + "\n")


### ORDERS ###

## Create order in db ## 
order_to_create = {"client_id":2, 
                    "order_products":"3", 
                    "order_price":"50$",
                    "order_status":"served",
                    "order_review":"lo taim",
                    "order_rate":"2/10"}
order_created = orderHandler.createOrderDB(order_to_create)
if order_to_create.order_review is not None:
    order_review = order_to_create.order_review
else:
    order_review = "no order review"

if order_to_create.order_rate is not None:
    order_rate = order_to_create.order_rate
else:
    order_rate = "no order review"

print("Order created on DB-" + "\n" +
        "client_id: " + order_created.client_id + "\n" +
        "order products: " + order_created.order_products + "\n" + 
        "order price: " + order_created.order_price + "\n" + 
        "order status: " + order_created.order_status + "\n" +
        "order review: " + order_review + "\n" +
        "order rate: " + order_rate + "\n"
        )

## Get order from db by id ##
order_by_id = orderHandler.getOrderDB(3)
if order_by_id.order_review is not None:
    order_review = order_by_id.order_review
else:
    order_review = "no order review"

if order_by_id.order_rate is not None:
    order_rate = order_by_id.order_rate
else:
    order_rate = "no order review"

print("client_id: " + order_by_id.client_id + "\n" +
         "order products: " + order_by_id.order_products + "\n" + 
         "order price: " + order_by_id.order_price + "\n" + 
         "order status: " + order_by_id.order_status + "\n" +
         "order review: " + order_review + "\n" +
         "order rate: " + order_rate + "\n"
        )


## Get all orders from db ##
all_orders = orderHandler.getAllOrdersDB(0)
for order in all_orders:
    if order.order_review is not None:
        order_review = order.order_review
    else:
        order_review = "no order review"

    if order.order_rate is not None:
        order_rate = order.order_rate
    else:
        order_rate = "no order review"
                
    print("client_id: " + order.client_id + "\n" +
             "order products: " + order.order_products + "\n" + 
             "order price: " + order.order_price + "\n" + 
             "order status: " + order.order_status + "\n" +
             "order review: " + order_review + "\n" +
             "order rate: " + order_rate + "\n")


## Update order in db ##
order_data = {
     "client_id" : 1,
     "order_products" : "3",
     "order_price" : "0$",
     "order_status" : "reopened",
     "order_review" : None,
     "order_rate" : None}
order_id = 1
updated_order = orderHandler.updateOrderDB(order_data=order_data, order_id=order_id)
        
if updated_order.order_review is not None:
        order_review = updated_order.order_review
else:
        order_review = "no order review"

if updated_order.order_rate is not None:
    order_rate = updated_order.order_rate
else:
    order_rate = "no order review"

print("client_id: " + str(updated_order.client_id) + "\n" +
        "order products: " + updated_order.order_products + "\n" + 
        "order price: " + updated_order.order_price + "\n" + 
        "order status: " + updated_order.order_status + "\n" +
        "order review: " + order_review + "\n" +
        "order rate: " + order_rate + "\n")

## Delete client from db by id##
order_deleted_by_id = orderHandler.deleteOrderDB(1)
if order_deleted_by_id.order_review is not None:
    order_review = order_deleted_by_id.order_review
else:
    order_review = "no order review"

if order_deleted_by_id.order_rate is not None:
    order_rate = order_deleted_by_id.order_rate
else:
    order_rate = "no order review"
print("client_id: " + str(order_deleted_by_id.client_id) + "\n" +
        "order products: " + order_deleted_by_id.order_products + "\n" + 
        "order price: " + order_deleted_by_id.order_price + "\n" + 
        "order status: " + order_deleted_by_id.order_status + "\n" +
        "order review: " + order_review + "\n" +
        "order rate: " + order_rate + "\n")


### MENU ITEMS ###

## Create item in db ##
item_to_create = { "item_name":"pasta", 
                "item_type":"food",
                 "item_price":"15$"}
item_created = itemHandler.createItemDB(item_to_create)

print("Item created on DB-" + "\n" +
        "item name: " + item_created.item_name + "\n" + 
        "item type: " + item_created.item_type + "\n" + 
        "item price: " + item_created.item_price + "\n"
        )

## Get item from db by id ##
item_by_id = itemHandler.getItemDB(1)
print("item name: " + item_by_id.item_name + "\n" + 
        "item type: " + item_by_id.item_type + "\n" + 
        "item price: " + item_by_id.item_price + "\n")

## Get all items from db ##
all_items = itemHandler.getAllItemsDB(0)
for item in all_items:                
    print("item name: " + item.item_name + "\n" + 
          "item type: " + item.item_type + "\n" + 
          "item price: " + item.item_price + "\n")


## Update item in db ##
item_data = {
        "item_name" : "coffee",
        "item_type" : "drink",
        "item_price" : "2$"}
item_id = 1
updated_item = itemHandler.updateItemDB(item_data=item_data, item_id=item_id)
        
print("item name: " + updated_item.item_name + "\n" + 
        "item type: " + updated_item.item_type + "\n" + 
        "item price: " + updated_item.item_price + "\n")

## Delete item from db by id##
item_deleted_by_id = itemHandler.deleteItemDB(1)
        
print("item name: " + item_deleted_by_id.item_name + "\n" + 
        "item type: " + item_deleted_by_id.item_type + "\n" + 
        "item price: " + item_deleted_by_id.item_price+"\n")
           

if __name__ == "__main__":
    app.run(port=8090) #הפורט שממנו יפעל 
