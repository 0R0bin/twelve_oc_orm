import click
import sentry_sdk
import sqlalchemy as db
import config_app.cli as cliGlobal
import config_app.controllers as ctrlGloal
import provider as p

from clients.cli import cli_client
from contracts.cli import cli_contract
from events.cli import cli_event
from users.cli import cli_user
from sqlalchemy import inspect
from sqlalchemy.orm import declarative_base, sessionmaker


def activation_sentry():
    sentry_sdk.init(
        dsn="https://deb0c84ce90a1d11b195c386a692d0aa@o4507182917812224.ingest.de.sentry.io/4507182921220176",
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        traces_sample_rate=1.0,
        # Set profiles_sample_rate to 1.0 to profile 100%
        # of sampled transactions.
        # We recommend adjusting this value in production.
        profiles_sample_rate=1.0,
    )


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
cli.add_command(cli_contract)
cli.add_command(cli_event)
cli.add_command(cli_user)


if __name__ == '__main__':
    activation_sentry()
    init_app()
    cli()
