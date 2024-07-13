from sqlalchemy import func
from models import MenuItem  # Assuming MenuItem is defined in models.py
from app import db

ERROR_NO_ITEM_FOUND_BY_ID = "Item not found, try using a different ID"
ERROR_NO_ITEMS_FOUND = "No items found"

class itemHandler:
    @staticmethod
    def createItemDB(item_data):
        new_item = MenuItem(
            item_id=itemHandler.generateId(),
            item_name=item_data["item_name"],
            item_type=item_data["item_type"],
            item_price=item_data["item_price"],
        )

        db.session.add(new_item)
        db.session.commit()
        return new_item

    @staticmethod
    def generateId():
        max_id = db.session.query(func.max(MenuItem.item_id)).scalar()
        next_id = (max_id or 0) + 1
        return next_id

    @staticmethod
    def getItemDB(item_id):
        item_to_return = MenuItem.query.filter_by(item_id=item_id).first()
        if item_to_return:
            return item_to_return
        else:
            return ERROR_NO_ITEM_FOUND_BY_ID

    @staticmethod
    def getAllItemsDB():
        items_to_return = MenuItem.query.all()
        if items_to_return:
            return items_to_return
        else:
            return ERROR_NO_ITEMS_FOUND

    @staticmethod
    def updateItemDB(item_data, item_id):
        item_to_update = MenuItem.query.filter_by(item_id=item_id).first()
        if item_to_update:
            for key, value in item_data.items():
                # Check if the attribute exists in the MenuItem model before updating
                if hasattr(item_to_update, key):
                    setattr(item_to_update, key, value)
        else:
            return ERROR_NO_ITEM_FOUND_BY_ID

        db.session.commit()
        return item_to_update

    @staticmethod
    def deleteItemDB(item_id):
        item_to_delete = MenuItem.query.filter_by(item_id=item_id).first()
        if item_to_delete:
            deleted_item = item_to_delete
            db.session.delete(item_to_delete)
            db.session.commit()
            return deleted_item
        else:
            return ERROR_NO_ITEM_FOUND_BY_ID
