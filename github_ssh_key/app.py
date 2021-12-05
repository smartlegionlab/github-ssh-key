#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# smartlegiondev@gmail.com
# --------------------------------------------------------
import click

from github_ssh_key.manager import CliManager


@click.group(
    invoke_without_command=True,
    context_settings={'help_option_names': ['-h', '--help']},
)
@click.version_option(f'{CliManager.name} v{CliManager.version}')
@click.pass_context
def cli(ctx):
    """
    Github ssh key manager.

    Copyright © 2018-2021, A.A Suvorov; All rights reserved.

    https://github.com/smartlegionlab

    """
    CliManager.show_head()
    if ctx.invoked_subcommand is None:
        CliManager.commander.run()


@cli.command(name='run')
def run():
    """Run Main menu."""
    CliManager.commander.run()


@cli.command(name='new')
@click.option('-e', 'email', type=click.STRING, default=None, help='Your email used on GitHub')
def new_key(email):
    """Create new public ssh keys."""
    CliManager.commander.new_key(email=email)


@cli.command(name='test')
def test_key():
    """Test your public ssh keys."""
    CliManager.commander.test_key()


@cli.command(name='show')
def show_key():
    """Show your public ssh keys."""
    CliManager.commander.show_key()


@cli.command(name='clone')
@click.option('-l', '--login', type=click.STRING, help='GitHub login', default=None)
@click.option('-n', '--name', type=click.STRING, help='Repo name', default=None)
def clone_repo(login, name):
    """Clone your GitHub repository using ssh."""
    CliManager.commander.clone_repo(login=login, repo_name=name)


@cli.command(name='add')
def add_key():
    """Open https://github.com/settings/keys in default browser"""
    CliManager.commander.add_key()


@cli.result_callback()
def process_result(result):
    """Process result"""
    CliManager.show_footer()


if __name__ == '__main__':
    cli()
