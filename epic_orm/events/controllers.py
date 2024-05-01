import provider as p

from events.models import EventModels as eModels


def create_event(info_event, contract):
    """ With information provided, save event in database """
    event_to_add = eModels.Event(
        nom=info_event['name'],
        date_start=info_event['date_start'],
        date_end=info_event['date_end'],
        location=info_event['location'],
        attendees=int(info_event['attendees']),
        notes=info_event['notes'],
        contract_id=contract.id,
        client_id=contract.client.id
        )
    p.session.add(event_to_add)
    p.session.commit()


def put_event(info_event, event):
    """ With information provided, put event in database """
    event.nom = info_event['name']
    event.date_start = info_event['date_start']
    event.date_end = info_event['date_end']
    event.location = info_event['location']
    event.attendees = info_event['attendees']
    event.notes = info_event['notes']

    p.session.commit()


def patch_event_supprt(id_support, event):
    """ With information provided, put event in database """
    event.support_id = id_support

    p.session.commit()


def get_all_events(filter, user):
    """
    Return all events in DB
    """
    result = p.session.query(eModels.Event).all()

    if filter == 1:
        result = p.session.query(eModels.Event).filter(eModels.Event.support_id is None)
    elif filter == 3:
        result = p.session.query(eModels.Event).filter(eModels.Event.support_id == user['id'])

    return result


def get_event_with_filter(info):
    """
    Return all events if choice == 1 by id, 2 by num, 3 by mail
    """
    choice_filter = int(info['choice'])

    if choice_filter == 1:
        result = p.session.query(eModels.Event).filter(eModels.Event.id == info['param']).first()
    if choice_filter == 2:
        result = p.session.query(eModels.Event).filter(eModels.Event.nom == info['param']).first()

    if result is None:
        return 404

    return result
