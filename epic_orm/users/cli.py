import click
import users.controllers as uCtrl
import users.views as uViews


@click.group(name='user')
def cli_user():
    """Click for user"""
    pass

@cli_user.command()
def create_user():
    """ Add User to DB """
    info_user = uViews.get_info_create_user()
    uCtrl.save_user_to_db(info_user)
    print(info_user)