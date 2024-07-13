from sqlalchemy import func
from models import Client
from app import db

ERROR_NO_CLIENT_FOUND_BY_ID = "Client not found, try use different id"
ERROR_NO_CLIENTS_FOUND = "No clients found"

class clientHandler:
    def createClientDB(client_data):
        new_client = Client(
            client_id = clientHandler.generateId(),
            user_name = client_data["user_name"],
            password = client_data["password"]
        )

        db.session.add(new_client)
        db.session.commit()
        return new_client

    @staticmethod
    def generateId():
        max_id = db.session.query(func.max(Client.client_id)).scalar()
        next_id = (max_id or 0) + 1
        return next_id

    def getClientDB(client_id):
        client_to_return = Client.query.filter_by(client_id=client_id).first()
        if client_to_return:
            return client_to_return
        else:
            return ERROR_NO_CLIENT_FOUND_BY_ID
        
    def getAllClientsDB(client_id):
        clients_to_return = Client.query.all()
        if clients_to_return:
            return clients_to_return
        else:
            return ERROR_NO_CLIENTS_FOUND

    
    def deleteClientDB(client_id):
        client_to_delete = Client.query.filter_by(client_id=client_id).first()
        if client_to_delete:
            deleted_client = client_to_delete
            db.session.delete(client_to_delete)
            db.session.commit()
            return deleted_client
        else:
            return ERROR_NO_CLIENT_FOUND_BY_ID
        


  