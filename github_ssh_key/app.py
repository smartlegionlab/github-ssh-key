#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
import click

from github_ssh_key.manager import CliMan


@click.group(
    invoke_without_command=True,
    context_settings={'help_option_names': ['-h', '--help']},
)
@click.version_option(f'{CliMan.name} v{CliMan.version}')
@click.pass_context
def cli(ctx):
    """
    Github ssh key manager.

    Copyright © 2018-2021, A.A Suvorov;

    Use:

    To access GitHub over ssh, you should run some sequence of actions.

    \b
    - Install openssh;
    - Generate new ssh keys;
    - Copy the public key;
    - Add your public key to GitHub;
    - Check the connection;

    This utility provides you with these capabilities.

    Principle of operation:

    - Create a new key using the interactive menu.
     During the creation process, do not change the default file name,
     since the utility is currently configured to work with the name
     file by default.

    Your keys will be stored in the folder: ~/.ssh/

    - Next, you will be prompted to add your key to your GitHub account.
     Answer in the affirmative.

    - Your key will be displayed in the console, copy it.

    - After that, you will be prompted to open the page for adding a key.
     The default browser will open with a page for adding a key.

    - Upload the copied key to GitHub.

    Go back to the console and select test the key.

    - Test the connection. If you see a greeting, then
     everything works correctly.

    Also, directly from the interactive menu, you can clone your private
    repository using ssh.

    To get help with commands, use:

    github-ssh-key [command] -h


    Copyright © 2018-2021, A.A Suvorov; All rights reserved.

    https://github.com/smartlegionlab

    """
    CliMan.show_head()
    if ctx.invoked_subcommand is None:
        CliMan.commander.run()


@cli.command(name='run')
def run():
    """Run Main menu."""
    CliMan.commander.run()


@cli.command(name='new')
@click.option('-e', 'email', type=click.STRING, default=None, help='Your email used on GitHub')
def ssh_key_new(email):
    """Create new public ssh keys."""
    CliMan.commander.new_key(email=email)


@cli.command(name='test')
def ssh_key_test():
    """Test your public ssh keys."""
    CliMan.commander.test_key()


@cli.command(name='show')
def ssh_key_show():
    """Show your public ssh keys."""
    CliMan.commander.show_key()


@cli.command(name='clone')
@click.option('-l', '--login', type=click.STRING, help='GitHub login', default=None)
@click.option('-n', '--name', type=click.STRING, help='Repo name', default=None)
def ssh_clone_repo(login, name):
    """Clone your GitHub repository using ssh."""
    CliMan.commander.clone_repo(login=login, repo_name=name)


@cli.command(name='github')
def ssh_key_show():
    """Open https://github.com/settings/keys in default browser"""
    CliMan.commander.open_github()


@cli.result_callback()
def process_result(result):
    """Process result"""
    CliMan.show_footer()


if __name__ == '__main__':
    cli()
