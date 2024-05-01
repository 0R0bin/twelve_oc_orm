import click
import config_app.auth_controller as cAC
import config_app.views as cViews
import clients.controllers as clCtrl
import clients.views as clViews


@click.group(name='client')
def cli_client():
    """Click Group for user"""
    pass

@cli_client.command()
def list_all():
    """ List All Clients In DB """
    authorized = cViews.check_perm([1, 2, 3])
    if authorized is False:
        return

    queryset = clCtrl.get_all_clients()
    clViews.list_all_clients(queryset)


@cli_client.command()
def create():
    """ Add User to DB """
    authorized = cViews.check_perm([2])
    if authorized is False:
        return

    user = cAC.get_user_info()

    info_client = clViews.get_info_user(True)
    clCtrl.create_client(info_client, user['id'])
    click.echo('Client ajouté')


@cli_client.command()
def modify():
    """ PUT User in DB """
    authorized = cViews.check_perm([2])
    if authorized is False:
        return

    user = cAC.get_user_info()
    info_filter = clViews.get_info_filter_client()
    client = clCtrl.get_client_with_filter(info_filter)

    if user == 404:
        click.echo('Client pas trouvé')
        return

    if user['id'] != client.contact_commercial_id:
        click.echo('Ce client ne vous appartient pas')
        return

    choice = clViews.confirm_client(client)

    if choice is False:
        click.echo('Modification annulée')
        return

    info_client = clViews.get_info_user(False)
    clCtrl.put_client(info_client, client)
    click.echo('Modification confirmée')

