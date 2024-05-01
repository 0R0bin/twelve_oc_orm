import click
import sqlalchemy as db
import config_app.cli as cliGlobal
import config_app.controllers as ctrlGloal
import provider as p

from users.cli import cli_user
from sqlalchemy import inspect
from sqlalchemy.orm import declarative_base, sessionmaker

def init_app():
    data = ctrlGloal.read_env_file()

    p.engine = db.create_engine(
        f"postgresql:///?user={data["DB_USER"]}&password={data["DB_PASS"]}&database={data["DB_NAME"]}&host={data["DB_HOST"]}&port={data["DB_PORT"]}", 
        echo=True)
    p.Base = declarative_base()
    p.session = sessionmaker(bind=p.engine)
    p.inspector = inspect(p.engine)


@click.group()
def cli():
    pass

cli.add_command(cliGlobal.create_tables)
cli.add_command(cli_user)
# cli.add_command(cliGlobal.login)
# cli.add_command(cliGlobal.logout)


if __name__ == '__main__':
    init_app()
    cli()