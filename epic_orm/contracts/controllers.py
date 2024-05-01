import provider as p

from contracts.models import ContractModels as ctModels


def get_all_contracts(filter):
    """
    Return all events in DB
    """
    result = p.session.query(ctModels.Contract).all()

    if filter == 1:
       result = p.session.query(ctModels.Contract).filter(ctModels.Contract.statut_signed == False)
    if filter == 2:
       result = p.session.query(ctModels.Contract).filter(ctModels.Contract.total_amount_left >= 0)

    return result

def create_contract(info_contract, id_client):
   """ With information provided, save event in database """
   contract_to_add = ctModels.Contract(
      unique_id=info_contract['unique_id'],
      total_amount=info_contract['total_amount'],
      total_amount_left=info_contract['total_amount_left'],
      client_id=id_client,
      )
   p.session.add(contract_to_add)
   p.session.commit()


def get_contract_with_filter(info):
   """
   Return all events if choice == 1 by id, 2 by num, 3 by mail
   """
   choice_filter = int(info['choice'])

   if choice_filter == 1:
      result = p.session.query(ctModels.Contract).filter(ctModels.Contract.id == info['param']).first()
   if choice_filter == 2:
      result = p.session.query(ctModels.Contract).filter(ctModels.Contract.unique_id == info['param']).first()

   if result is None:
      return 404

   return result

def put_contract(info_contract, contract):
   """ With information provided, put user in database """
   contract.unique_id = info_contract['unique_id']
   contract.total_amount = info_contract['total_amount']
   contract.total_amount_left = info_contract['total_amount_left']

   p.session.commit()