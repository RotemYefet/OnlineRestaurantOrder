from app import db

class Client(db.Model):
    __tablename__ = "Client"

    client_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    
    def json(self):
        return {
            "client_id": self.client_id,
            "user_name": self.user_name,
            "password": self.password,
        }

class Order(db.Model):
    __tablename__ = "Order"

    order_id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, nullable=False)
    order_products = db.Column(db.String(100), nullable=False)
    order_price = db.Column(db.String(100), nullable=False)
    order_status = db.Column(db.String(100), nullable=False)
    order_review = db.Column(db.String(100), nullable=True)
    order_rate = db.Column(db.Integer, nullable=True)


    def json(self):
        return {
            "order_id" : self.order_id,
            "client_id" : self.client_id,
            "order_products" : self.order_products,
            "order_price" : self.order_price,
            "order_status" : self.order_status,
            "order_review" : self.order_review,
            "order_rate" : self.order_rate,
        }


class MenuItem(db.Model):
    __tablename__ = "MenuItem"

    item_id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    item_type = db.Column(db.String(100), nullable=False)
    item_price = db.Column(db.String(100), nullable=False)


    def json(self):
        return {
            "item_id" : self.item_id,
            "item_name" : self.item_name,
            "item_type" : self.item_type,
            "item_price" : self.item_price,
        }
