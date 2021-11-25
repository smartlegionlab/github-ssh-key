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
import os
from pathlib import Path

import click
from smartcliapp import CliManager


class Commander:

    def __init__(self):
        self._cli_man = CliManager()

    def run(self):
        while 1:
            self._cli_man.printer.smart.echo("Main Menu", char="=")
            self._cli_man.printer.base.echo('If you have any problems, press h to read the help.')
            self._cli_man.printer.smart.echo()
            msg = 'n: new key\n'
            msg += 's: show key\n'
            msg += 'a: add to github\n'
            msg += 't: test key\n'
            msg += 'c: clone repo\n'
            msg += 'h: help\n'
            msg += 'q: quit'
            self._cli_man.printer.base.echo(msg)
            self._cli_man.printer.smart.echo()
            char = click.getchar()

            if char in ('q', 'й'):
                self.quit()
                break

            if char in ('n', 'т'):
                self.new_key()
            elif char in ('s', 'ы'):
                self.show_key()
            elif char in ('a', 'ф'):
                self.add_key()
            elif char in ('t', 'е'):
                self.test_key()
            elif char in ('c', 'с'):
                self.clone_repo()
            elif char in ('h', 'р'):
                self.open_help()
            else:
                self._cli_man.printer.smart.echo()
                self._cli_man.printer.base.echo('Invalid input')

    def new_key(self, email=None):
        self._cli_man.printer.smart.echo('Ssh key create')
        self._cli_man.printer.smart.echo()
        if email is None:
            email = input('Enter your email: ')

        self._cli_man.printer.smart.echo()

        command = f'ssh-keygen -t ed25519 -C "{email}"'
        command2 = f'eval "$(ssh-agent -s)"'
        command3 = 'ssh-add ~/.ssh/id_ed25519'

        status = os.system(f'{command} && {command2} && {command3}')

        if not bool(status):
            self._cli_man.printer.smart.echo()
            if self._cli_man.get_action('Add new key to github?'):
                self.add_key()

            if self._cli_man.get_action('Test your ssh key?'):
                self.test_key()
        else:
            self._cli_man.printer.smart.echo()
            self._cli_man.printer.base.echo('An error occurred while working, read help.')
            if self._cli_man.get_action('Open help?'):
                self.open_help()

    def show_key(self):
        path = f'{Path.home()}/.ssh/id_ed25519.pub'
        key = self._get_key()
        self._cli_man.printer.smart.echo('Show ssh public key:')
        self._cli_man.printer.base.echo('Highlight and completely copy your ssh key.')
        if key:
            self._cli_man.printer.base.echo()
            self._cli_man.printer.base.echo(key)
        else:
            self._cli_man.printer.base.echo(f'Error! File {path} - Not found!')
            self._cli_man.printer.base.echo(f'- Do not change the default file name.')
        self._to_continue()

    def add_key(self):
        self.show_key()
        self._cli_man.printer.smart.echo('Open https://github.com/settings/keys')
        self._cli_man.printer.base.echo('- The default browser will now launch.')
        self._cli_man.printer.base.echo('- This will open a page to add the ssh key to your GitHub account.')
        self._cli_man.printer.smart.echo()
        self._cli_man.to_continue('Enter to continue...')
        self._cli_man.printer.smart.echo()
        self._cli_man.printer.base.echo('Launching the browser ... ')
        self._cli_man.printer.smart.echo()
        self._cli_man.launch('https://github.com/settings/keys')

    def test_key(self):
        self._cli_man.printer.smart.echo('Testing the Github connection: ')
        self._cli_man.printer.base.echo('Wait...')
        self._cli_man.printer.base.echo('Receiving the information...')
        self._cli_man.printer.smart.echo()
        os.system('ssh-keyscan github.com >> ~/.ssh/known_hosts')
        self._cli_man.printer.smart.echo()
        os.system('ssh -T git@github.com')
        self._to_continue()

    def clone_repo(self, login=None, repo_name=None):
        self._cli_man.printer.smart.echo('Clone repo: ')
        if login is None:
            login = self._cli_man.input('Enter you GitHub login: ')
        if repo_name is None:
            repo_name = self._cli_man.input('Enter your repo name: ')
        command = f'git clone git@github.com:{login}/{repo_name}.git'
        self._cli_man.printer.base.echo(f'Execute: {command}')
        os.system(f'git clone git@github.com:{login}/{repo_name}.git')
        self._cli_man.to_continue()

    def _to_continue(self):
        self._cli_man.printer.smart.echo()
        input('Enter to continue...')

    def open_help(self):
        while True:
            self._cli_man.printer.smart.echo('Help url: https://github.com/smartlegionlab/github-ssh-key')
            self._cli_man.printer.smart.echo('Help:')
            self._cli_man.printer.smart.echo('Adding a key to your GitHub account involves several steps:')
            self._cli_man.printer.base.echo('g: generating new ssh key.')
            self._cli_man.printer.base.echo('c: copying ssh key.')
            self._cli_man.printer.base.echo('a: adding ssh key to your GitHub account.')
            self._cli_man.printer.base.echo('t: testing the ssh key (Testing the connection).')
            self._cli_man.printer.base.echo('b: back to main menu.')
            self._cli_man.printer.smart.echo()
            char = click.getchar()

            if char in ('b', 'и'):
                break

            if char in ('g', 'п'):
                self._new_help()
            elif char in ('c', 'с'):
                self._copy_help()
            elif char in ('a', 'ф'):
                self._add_help()
            elif char in ('t', 'е'):
                self._test_help()
            else:
                continue
            self._cli_man.to_continue()

    def _new_help(self):
        self._cli_man.printer.smart.echo('Generating new ssh key:')
        self._cli_man.printer.base.echo('- Install openssh, or make sure you have it installed with the ssh command.')
        self._cli_man.printer.base.echo('- During the generation process, enter your email that you '
                                        'use when working with GitHub.')
        self._cli_man.printer.base.echo('- Do not change the default file name.')
        self._cli_man.printer.base.echo("- Don't set a passphrase if you don't want to enter it every time.")
        self._cli_man.printer.smart.echo()

    def _copy_help(self):
        self._cli_man.printer.smart.echo('Copying ssh key:')
        self._cli_man.printer.base.echo('- Highlight and completely copy your ssh key.')
        self._cli_man.printer.smart.echo()

    def _add_help(self):
        self._cli_man.printer.smart.echo('Adding ssh key to your GitHub account:')
        self._cli_man.printer.base.echo('- Highlight and completely copy your ssh key.')
        self._cli_man.printer.base.echo('- Add your ssh key to your GitHub account.')
        self._cli_man.printer.smart.echo()

    def _test_help(self):
        self._cli_man.printer.smart.echo('Testing the ssh key (Testing the connection):')
        self._cli_man.printer.base.echo('For a successful connection, you had to follow these steps:')
        self._cli_man.printer.base.echo('- Generate ssh key.')
        self._cli_man.printer.base.echo('- Highlight and completely copy your ssh key.')
        self._cli_man.printer.base.echo('- Add ssh key to your GitHub account.')
        self._cli_man.printer.base.echo('If you did everything correctly, you will see a personalized greeting.')
        self._cli_man.printer.smart.echo()

    @staticmethod
    def _get_key():
        path = f'{Path.home()}/.ssh/id_ed25519.pub'
        if Path(path).exists():
            with open(f'{Path.home()}/.ssh/id_ed25519.pub', 'r') as f:
                text = f.read()
                return text
        return False

    def quit(self):
        pass
