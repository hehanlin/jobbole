# -*- coding: utf-8 -*-

import click
from common.sqlalchemy import create_tables


@click.group()
@click.help_option(help="database manger")
def db():
    pass


@click.command()
def db_init():
    create_tables()

db.add_command(db_init, name='init')


@click.group()
@click.help_option(help="jobbole command manger")
def main():
    pass

main.add_command(db, name='db')

if __name__ == "__main__":
    main()

