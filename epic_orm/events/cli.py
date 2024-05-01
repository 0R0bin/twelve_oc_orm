import click
import config_app.auth_controller as cAC
import config_app.views as cViews
import contracts.controllers as ctCtrl
import contracts.views as ctViews
import events.controllers as eCtrl
import events.views as eViews
import users.controllers as uCtrl
import users.views as uViews


@click.group(name='event')
def cli_event():
    """Click Group for Event"""
    pass


@cli_event.command()
@click.argument("filter", type=bool, default=False)
def list_all(filter):
    """
    List All Event In DB\n
    [ARGUMENT] filter\n
    You can add "True" to command, depending on your role, filter will be applied
    """
    authorized = cViews.check_perm([1, 2, 3])
    if authorized is False:
        return

    queryset = eCtrl.get_all_events(0, None)

    if filter is True:
        user = cAC.get_user_info()
        if user['role'] == 1:
            queryset = eCtrl.get_all_events(1, None)
        if user['role'] == 3:
            queryset = eCtrl.get_all_events(3, user)

    eViews.list_all_events(queryset)


@cli_event.command()
def create():
    """ Add Event to DB """
    authorized = cViews.check_perm([2])
    if authorized is False:
        return

    info_event = eViews.get_info_event(True)
    info_filter = ctViews.get_info_filter_contract()
    contract = ctCtrl.get_contract_with_filter(info_filter)
    if contract == 404:
        click.echo('Contrat introuvable')
        return
    eCtrl.create_event(info_event, contract)
    click.echo('Evènement ajouté')


@cli_event.command()
def modify():
    """ PUT Event to DB """
    authorized = cViews.check_perm([1, 3])
    if authorized is False:
        return

    user = cAC.get_user_info()

    info_filter = eViews.get_info_filter_event(False)
    event = eCtrl.get_event_with_filter(info_filter)

    if event == 404:
        click.echo('Evènement introuvable')
        return

    choice = eViews.confirm_event(event)

    if choice is False:
        click.echo('Modification annulée')
        return

    # Si l'utilisateur est un Gestion
    if user['role'] == 1:
        queryset = uCtrl.get_all_users(3)
        click.echo('\n========Liste utilisateurs Département Support========')
        uViews.list_all_users(queryset)
        info_filter = uViews.get_info_filter_user(None)
        user = uCtrl.get_user_with_filter(info_filter)

        if user == 404:
            click.echo('Utilisateur introuvable')
            return
        eCtrl.patch_event_supprt(user.id, event)
    # Si l'utilisateur est un Support
    else:
        if event.support_id != user['id']:
            click.echo('Vous n\'êtes pas afecté à cet évènement')
            return

        info_event = eViews.get_info_event(False)
        eCtrl.put_event(info_event, event)

    click.echo('Modification confirmée')
