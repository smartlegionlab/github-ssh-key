# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
import os
from pathlib import Path

import click
from smartcliapp import CliManager


class Commander:
    _cli_man = CliManager()

    @classmethod
    def run(cls):
        while 1:
            cls._cli_man.printer.smart.echo("Main Menu", char="=")
            cls._cli_man.printer.base.echo('n: new key')
            cls._cli_man.printer.base.echo('s: show key')
            cls._cli_man.printer.base.echo('t: test key')
            cls._cli_man.printer.base.echo('o: open github')
            cls._cli_man.printer.base.echo('c: clone repo')
            cls._cli_man.printer.base.echo('h: help')
            cls._cli_man.printer.base.echo('q: quit')
            cls._cli_man.printer.smart.echo()
            char = click.getchar()

            if char in ('q', 'й'):
                cls.quit()
                break

            if char in ('n', 'т'):
                cls.new_key()
            elif char in ('s', 'ы'):
                cls.show_key()
            elif char in ('t', 'е'):
                cls.test_key()
            elif char in ('c', 'с'):
                cls.clone_repo()
            elif char in ('h', 'р'):
                cls.open_help()
            elif char in ('o', 'щ'):
                cls.open_github()
            else:
                cls._cli_man.printer.smart.echo()
                cls._cli_man.printer.base.echo('Invalid input')

    @classmethod
    def open_github(cls):
        cls._cli_man.printer.smart.echo('Open https://github.com/settings/keys')
        cls._cli_man.printer.base.echo('Launching the browser ... ')
        cls._cli_man.launch('https://github.com/settings/keys')

    @classmethod
    def new_key(cls, email=None):
        cls._cli_man.printer.smart.echo('Ssh key create')
        if email is None:
            email = input('Enter your email: ')
        command = f'ssh-keygen -t ed25519 -C "{email}"'
        command2 = f'eval "$(ssh-agent -s)"'
        command3 = 'ssh-add ~/.ssh/id_ed25519'
        os.system(f'{command} && {command2} && {command3}')
        cls._cli_man.printer.smart.echo()
        action = cls._cli_man.get_action('Add new key to github?')
        if action:
            cls.show_key()
            cls._cli_man.printer.smart.echo()
            action = cls._cli_man.get_action('Launch a browser and open a page for adding a key?')
            if action:
                cls.open_github()

    @classmethod
    def show_key(cls):
        cls._cli_man.printer.smart.echo('Show ssh public key')
        path = f'{Path.home()}/.ssh/id_ed25519.pub'
        key = cls._get_key()
        if key:
            cls._cli_man.printer.base.echo('Copy your public key: ')
            cls._cli_man.printer.base.echo()
            cls._cli_man.printer.base.echo(key)
        else:
            cls._cli_man.printer.base.echo(f'Error! Path: {path} - Not found!')
        cls._to_continue()

    @classmethod
    def test_key(cls):
        cls._cli_man.printer.smart.echo('Testing the Github connection')
        cls._cli_man.printer.base.echo('Wait...')
        cls._cli_man.printer.base.echo('Receiving the information...')
        cls._cli_man.printer.smart.echo()
        os.system('ssh-keyscan github.com >> ~/.ssh/known_hosts')
        cls._cli_man.printer.smart.echo()
        os.system('ssh -T git@github.com')
        cls._to_continue()

    @classmethod
    def clone_repo(cls, login=None, repo_name=None):
        cls._cli_man.printer.smart.echo('Clone repo: ')
        if login is None:
            login = cls._cli_man.input('Enter you GitHub login: ')
        if repo_name is None:
            repo_name = cls._cli_man.input('Enter your repo name: ')
        command = f'git clone git@github.com:{login}/{repo_name}.git'
        cls._cli_man.printer.base.echo(f'Execute: {command}')
        os.system(f'git clone git@github.com:{login}/{repo_name}.git')

    @classmethod
    def _get_key(cls):
        path = f'{Path.home()}/.ssh/id_ed25519.pub'
        if Path(path).exists():
            with open(f'{Path.home()}/.ssh/id_ed25519.pub', 'r') as f:
                text = f.read()
                return text
        return False

    @classmethod
    def _to_continue(cls):
        cls._cli_man.printer.smart.echo()
        input('Enter to continue...')

    @classmethod
    def open_help(cls):
        cls._cli_man.printer.smart.echo('Help:')
        cls._cli_man.printer.base.echo('Principle of operation: ')
        cls._cli_man.printer.base.echo('1. Create a new key.')
        cls._cli_man.printer.base.echo('2. Copy the key.')
        cls._cli_man.printer.base.echo('3. Add the key to GitHub.')
        cls._cli_man.printer.base.echo('4. Test the connection.')
        cls._cli_man.printer.base.echo('5. Work with GutHub over SSH.')
        cls._cli_man.printer.base.echo('Help url: https://github.com/smartlegionlab/github-ssh-key')
        cls._to_continue()

    @classmethod
    def quit(cls):
        cls._cli_man.printer.base.echo('Exit...')
