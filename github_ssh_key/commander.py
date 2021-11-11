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
from smartcliapp.managers import ClickMan


class Commander:
    _click_man = ClickMan()

    @classmethod
    def run(cls):
        while 1:
            cls._click_man.printer.smart.echo("Main Menu", char="=")
            cls._click_man.printer.base.echo('n: new key')
            cls._click_man.printer.base.echo('s: show key')
            cls._click_man.printer.base.echo('t: test key')
            cls._click_man.printer.base.echo('o: open github')
            cls._click_man.printer.base.echo('c: clone repo')
            cls._click_man.printer.base.echo('h: help')
            cls._click_man.printer.base.echo('q: quit')
            cls._click_man.printer.smart.echo()
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
                cls._click_man.printer.smart.echo()
                cls._click_man.printer.base.echo('Invalid input')

    @classmethod
    def open_github(cls):
        cls._click_man.printer.smart.echo('Open https://github.com/settings/keys')
        cls._click_man.printer.base.echo('Launching the browser ... ')
        cls._click_man.launch_man.launch('https://github.com/settings/keys')

    @classmethod
    def new_key(cls, email=None):
        cls._click_man.printer.smart.echo('Ssh key create')
        if email is None:
            email = input('Enter your email: ')
        command = f'ssh-keygen -t ed25519 -C "{email}"'
        command2 = f'eval "$(ssh-agent -s)"'
        command3 = 'ssh-add ~/.ssh/id_ed25519'
        os.system(f'{command} && {command2} && {command3}')
        cls._click_man.printer.smart.echo()
        action = cls._click_man.action_man.get_action('Add new key to github?')
        if action:
            cls.show_key()
            cls._click_man.printer.smart.echo()
            action = cls._click_man.action_man.get_action('Launch a browser and open a page for adding a key?')
            if action:
                cls.open_github()

    @classmethod
    def show_key(cls):
        cls._click_man.printer.smart.echo('Show ssh public key')
        path = f'{Path.home()}/.ssh/id_ed25519.pub'
        key = cls._get_key()
        if key:
            cls._click_man.printer.base.echo('Copy your public key: ')
            cls._click_man.printer.base.echo()
            cls._click_man.printer.base.echo(key)
        else:
            cls._click_man.printer.base.echo(f'Error! Path: {path} - Not found!')
        cls._to_continue()

    @classmethod
    def test_key(cls):
        cls._click_man.printer.smart.echo('Testing the Github connection')
        cls._click_man.printer.base.echo('Wait...')
        cls._click_man.printer.base.echo('Receiving the information...')
        cls._click_man.printer.smart.echo()
        os.system('ssh-keyscan github.com >> ~/.ssh/known_hosts')
        cls._click_man.printer.smart.echo()
        os.system('ssh -T git@github.com')
        cls._to_continue()

    @classmethod
    def clone_repo(cls, login=None, repo_name=None):
        cls._click_man.printer.smart.echo('Clone repo: ')
        if login is None:
            login = cls._click_man.input_man.input('Enter you GitHub login')
        if repo_name is None:
            repo_name = cls._click_man.input_man.input('Enter your repo name')
        command = f'git clone git@github.com:{login}/{repo_name}.git'
        cls._click_man.printer.base.echo(f'Execute: {command}')
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
        cls._click_man.printer.smart.echo()
        input('Enter to continue...')

    @classmethod
    def open_help(cls):
        cls._click_man.printer.smart.echo('Help:')
        cls._click_man.printer.base.echo('Principle of operation: ')
        cls._click_man.printer.base.echo('1. Create a new key.')
        cls._click_man.printer.base.echo('2. Copy the key.')
        cls._click_man.printer.base.echo('3. Add the key to GitHub.')
        cls._click_man.printer.base.echo('4. Test the connection.')
        cls._click_man.printer.base.echo('5. Work with GutHub over SSH.')
        cls._click_man.printer.base.echo('Help url: https://github.com/smartlegionlab/github-ssh-key')
        cls._to_continue()

    @classmethod
    def quit(cls):
        cls._click_man.printer.base.echo('Exit...')
