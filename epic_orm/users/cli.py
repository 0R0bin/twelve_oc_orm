import click
import config_app.views as cViews
import users.controllers as uCtrl
import users.views as uViews


@click.group(name='user')
def cli_user():
    """Click Group for user"""
    pass

@cli_user.command()
def list_all():
    """ List All Users In DB """
    authorized = cViews.check_perm([1])
    if authorized is False:
        return

    queryset = uCtrl.get_all_users(0)
    uViews.list_all_users(queryset)

@cli_user.command()
def create():
    """ Add User to DB """
    authorized = cViews.check_perm([1])
    if authorized is False:
        return

    info_user = uViews.get_info_user(True)
    uCtrl.save_user_to_db(info_user)
    click.echo('Utilisateur ajouté')


@cli_user.command()
def delete():
    """ Delete User in DB """
    authorized = cViews.check_perm([1])
    if authorized is False:
        return

    info_filter = uViews.get_info_filter_user(True)
    user = uCtrl.get_user_with_filter(info_filter)

    if user == 404:
        click.echo('Utilisateur pas trouvé')
        return

    choice = uViews.confirm_user(user)

    if choice is True:
        uCtrl.del_user(user)
        click.echo('Utilisateur supprimé')
        return

    click.echo('Suppression annulée')


@cli_user.command()
def modify():
    """ PUT User in DB """
    authorized = cViews.check_perm([1])
    if authorized is False:
        return

    info_filter = uViews.get_info_filter_user(False)
    user = uCtrl.get_user_with_filter(info_filter)

    if user == 404:
        click.echo('Utilisateur pas trouvé')
        return
    
    choice = uViews.confirm_user(user)

    if choice is False:
        click.echo('Modification annulée')
        return

    info_user = uViews.get_info_user(False)
    uCtrl.put_user(info_user, user)
    click.echo('Modification confirmée')

