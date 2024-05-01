import datetime
import provider as p

from clients.models import ClientModels as clModels


def get_all_clients():
    """
    Return all clients in DB
    """
    result = p.session.query(clModels.Client).all()

    return result


def get_client_with_filter(info):
    """
    Return le client en fonction du filtre séléctionné
    """
    choice_filter = int(info['choice'])

    if choice_filter == 1:
        result = p.session.query(clModels.Client).filter(clModels.Client.id == info['param']).first()
    if choice_filter == 2:
        result = p.session.query(clModels.Client).filter(clModels.Client.complete_name == info['param']).first()
    if choice_filter == 3:
        result = p.session.query(clModels.Client).filter(clModels.Client.email == info['param']).first()

    if result is None:
        return 404

    return result


def put_client(info, client):
    """ With information provided, put client in database """
    client.complete_name = info['complete_name']
    client.email = info['email']
    client.phone = info['phone']
    client.enterprise_name = info['enterprise_name']
    client.last_update_at = datetime.datetime.now()

    p.session.commit()


def create_client(info_client, user_id):
    """ With information provided, save client in database """
    client_to_add = clModels.Client(
        complete_name=info_client['complete_name'],
        email=info_client['email'],
        phone=info_client['phone'],
        enterprise_name=info_client['enterprise_name'],
        contact_commercial_id=int(user_id))

    p.session.add(client_to_add)
    p.session.commit()
