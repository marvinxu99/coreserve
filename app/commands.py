# app/commands.py

import click
from flask import current_app
from app.extensions import db
from app.db_utils import init_code_set_, db_fix_, create_test_users_


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


@click.command("create-users")
def create_test_uers():
    """ Create test users
    """
    with current_app.app_context():
        create_test_users_(db)
        print("Command run successfully.")


def register_commands(app):
    app.cli.add_command(init_code_set)
    app.cli.add_command(db_fix)
    app.cli.add_command(create_test_uers)
