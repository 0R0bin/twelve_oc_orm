import click
import config_app.controllers as caCtrls


@click.command()
def init_db():
    """ Create tables at first use"""
    caCtrls.create_tables_db()
    caCtrls.add_roles()
    click.echo('Base de données initialisée')

@click.command()
@click.argument("email", type=str, required=True)
@click.password_option()
def login(email, password):
    """ Login User """
    caCtrls.get_user_from_mail_pass(email, password)
    app.login(**kwargs)
    app.epic.database_disconnect()