import click
import sqlalchemy as db
import config_app.cli as cliGlobal
import config_app.controllers as ctrlGloal
import provider as p

from clients.cli import cli_client
from events.cli import cli_event
from users.cli import cli_user
from sqlalchemy import inspect
from sqlalchemy.orm import declarative_base, sessionmaker

# WITH HELP OF https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_updating_objects.htm

def init_app():
    data = ctrlGloal.read_env_file()

    p.engine = db.create_engine(
        f"postgresql:///?user={data["DB_USER"]}&password={data["DB_PASS"]}&database={data["DB_NAME"]}&host={data["DB_HOST"]}&port={data["DB_PORT"]}", 
        echo=False)
    p.Base = declarative_base()
    Session = sessionmaker(bind=p.engine)
    p.session = Session()
    p.inspector = inspect(p.engine)


@click.group()
def cli():
    pass

cli.add_command(cliGlobal.init_db)
cli.add_command(cliGlobal.login)
cli.add_command(cliGlobal.logout)
cli.add_command(cli_client)
cli.add_command(cli_event)
cli.add_command(cli_user)


if __name__ == '__main__':
    init_app()
    cli()