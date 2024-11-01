# app/commands.py

import click
from flask import current_app
from app.extensions import db
from app.db_utils.__generate_code_sets import init_code_set_
from app.db_utils.__db_fix_fields import db_fix_


@click.command("init-code-set")
@click.option('--verbose', is_flag=True, help="Enables verbose mode")
def init_code_set(verbose):
    """Initialize the code set in the database.
    """
    with current_app.app_context():
        init_code_set_(db)
        if verbose:
            print("Verbose mode enabled: Initializing code set...")
        print("Code set initialized successfully.")


@click.command("db-fix")
@click.option('--verbose', is_flag=True, help="Enables verbose mode")
def db_fix(verbose):
    """ fix db issues.
    """
    with current_app.app_context():
        db_fix_(db)
        if verbose:
            print("Verbose mode enabled: Initializing code set...")
        print("Command run successfully.")

