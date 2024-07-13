from sqlalchemy import func
from models import Order
from app import db

ERROR_NO_ORDER_FOUND_BY_ID = "Order not found, try use different id"
ERROR_NO_ORDERS_FOUND = "No orders found"

class orderHandler:
    def createOrderDB(order_data):
        new_order = Order(
            order_id = orderHandler.generateId(),
            client_id = order_data["client_id"],
            order_products = order_data["order_products"],
            order_price = order_data["order_price"],
            order_status = order_data["order_status"],
            order_review = order_data["order_review"],
            order_rate = order_data["order_rate"]
        
        )

        db.session.add(new_order)
        db.session.commit()
        return new_order

    @staticmethod
    def generateId():
        max_id = db.session.query(func.max(Order.order_id)).scalar()
        next_id = (max_id or 0) + 1
        return next_id

    def getOrderDB(order_id):
        order_to_return = Order.query.filter_by(order_id=order_id).first()
        if order_to_return:
            return order_to_return
        else:
            return ERROR_NO_ORDER_FOUND_BY_ID
        
    def getAllOrdersDB(order_id):
        orders_to_return = Order.query.all()
        if orders_to_return:
            return orders_to_return
        else:
            return ERROR_NO_ORDERS_FOUND
    

    def updateOrderDB(order_data, order_id):
        order_to_update = Order.query.filter_by(order_id=order_id).first()
        if order_to_update:
            for key, value in order_data.items():
                # Check if the attribute exists in the Order model before updating
                if hasattr(order_to_update, key):
                    setattr(order_to_update, key, value)
        else:
            return ERROR_NO_ORDER_FOUND_BY_ID
        
        db.session.commit()
        return order_to_update
        
        

    def deleteOrderDB(order_id):
        order_to_delete = Order.query.filter_by(order_id=order_id).first()
        if order_to_delete:
            deleted_order = order_to_delete
            db.session.delete(order_to_delete)
            db.session.commit()
            return deleted_order
        else:
            return ERROR_NO_ORDER_FOUND_BY_ID
        


  