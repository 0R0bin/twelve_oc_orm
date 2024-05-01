import click
import config_app.auth_controller as caAuthCtrl
import config_app.controllers as caCtrls
import config_app.views as caViews
import users.controllers as uCtrls


@click.command()
def init_db():
    """ Create tables at first use"""
    caCtrls.create_tables_db()
    caViews.add_roles()
    caCtrls.add_roles()
    caViews.add_first_user()
    caCtrls.add_first_user()
    click.echo('Base de données initialisée')


@click.command()
@click.argument("email", type=str, required=True)
@click.password_option()
def login(email, password):
    """ Login User | [OPTIONS] email"""
    user = uCtrls.get_user_from_mail_pass(email, password)

    if user == 404:
        click.echo('Votre mail n\'est pas reconnu')
        return

    if user == 401:
        click.echo('Mot de passe incorrect')
        return

    caAuthCtrl.gen_jwt_with_user_info(user)
    click.echo('Connexion réussie')


@click.command()
def logout():
    """ Logout User """
    caAuthCtrl.del_jwt()
    click.echo('Déconnexion réussie')
