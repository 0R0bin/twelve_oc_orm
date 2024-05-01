import click
import config_app.auth_controller as cAC
import config_app.views as cViews
import clients.controllers as clCtrl
import clients.views as clViews
import contracts.controllers as ctCtrl
import contracts.views as ctViews
# import users.controllers as uCtrl
# import users.views as uViews


@click.group(name='contract')
def cli_contract():
    """Click Group for Event"""
    pass

@cli_contract.command()
@click.argument("filter", type=int, default=0)
def list_all(filter):
    """
    List All Contracts In DB\n
    [ARGUMENT] filter\n
    You can add 1 to retrieve all contracts not signed\n
    Or 2 to retreive all contracts  not paid 
    """
    authorized = cViews.check_perm([1, 2, 3])
    if authorized is False:
        return

    queryset = ctCtrl.get_all_contracts(0)

    if filter in [1, 2]:
        user = cAC.get_user_info()
        if user['role'] == 2:
            if filter == 1:
                queryset = ctCtrl.get_all_contracts(1)
            if filter == 2:
                queryset = ctCtrl.get_all_contracts(2)

    ctViews.list_all_clients(queryset)


@cli_contract.command()
def create():
    """ Add Contract to DB """
    authorized = cViews.check_perm([1])
    if authorized is False:
        return

    info_contract = ctViews.get_info_contract(True)
    click.echo('Merci de choisir un client')
    # Affichage des clients
    queryset = clCtrl.get_all_clients()
    clViews.list_all_clients(queryset)
    # Choix du client
    info_filter = clViews.get_info_filter_client(False)
    client = clCtrl.get_client_with_filter(info_filter)

    if client == 404:
        click.echo('Client pas trouvé')
        return

    ctCtrl.create_contract(info_contract, client.id)
    click.echo('Contrat ajouté')


@cli_contract.command()
def modify():
    """ PUT Contract to DB """
    authorized = cViews.check_perm([1, 2])
    if authorized is False:
        return
    
    user = cAC.get_user_info()

    info_filter = ctViews.get_info_filter_contract()
    contract = ctCtrl.get_contract_with_filter(info_filter)

    if contract == 404:
        click.echo('Contrat introuvable')
        return

    choice = ctViews.confirm_contract(contract)

    if choice is False:
        click.echo('Modification annulée')
        return

    # Si l'utilisateur est un Gestion
    if user['role'] == 2:
        if user['id'] != contract.client.contact_commercial_id:
            click.echo('Vous n\'êtes pas afecté à ce client')
            return

    info_contract = ctViews.get_info_contract(False)
    ctCtrl.put_contract(info_contract)
    click.echo('Modification confirmée')