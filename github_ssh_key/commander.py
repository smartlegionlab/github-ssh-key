# -*- coding: utf-8 -*-
# -------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# -------------------------------------------------------
# https://github.com/smartlegionlab
# smartlegiondev@gmail.com
# -------------------------------------------------------
import os
from pathlib import Path

import click
from smartcliapp import CliManager


class Commander:
    def __init__(self):
        self._cli_man = CliManager()
        self._url = 'https://github.com/settings/keys'

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
                print('Invalid input!')

    def new_key(self, email=None):
        self._cli_man.printer.smart.echo('Ssh key create:', '=')
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
            print('An error occurred while working, read help.')
            if self._cli_man.get_action('Open help?'):
                self.open_help()

    def show_key(self):
        path = f'{Path.home()}/.ssh/id_ed25519.pub'
        key = self._get_key()
        self._cli_man.printer.smart.echo('Show ssh public key:', '=')
        print('\nHighlight and completely copy your ssh key.')
        if key:
            print(f'\n{key}')
        else:
            print(f'Error! File {path} - Not found!')
            print(f'- Do not change the default file name.')
        self._cli_man.printer.smart.echo()
        self._cli_man.to_continue()

    def add_key(self):
        self._cli_man.printer.smart.echo('Add key:', '=')
        self.show_key()
        self._cli_man.printer.smart.echo(f'Open {self._url}')
        print('- The default browser will now launch.')
        print('- This will open a page to add the ssh key to your GitHub account.')
        self._cli_man.printer.smart.echo()
        self._cli_man.to_continue()
        self._cli_man.printer.smart.echo()
        print('Launching the browser ... ')
        self._cli_man.printer.smart.echo()
        self._cli_man.launch(f'{self._url}')

    def test_key(self):
        self._cli_man.printer.smart.echo('Testing the Github connection:', '=')
        print('Wait...')
        print('Receiving the information...')
        self._cli_man.printer.smart.echo()
        os.system('ssh-keyscan github.com >> ~/.ssh/known_hosts')
        self._cli_man.printer.smart.echo()
        os.system('ssh -T git@github.com')
        self._cli_man.printer.smart.echo()
        self._cli_man.to_continue()

    def clone_repo(self, login=None, repo_name=None):
        self._cli_man.printer.smart.echo('Clone repo:', '=')
        if login is None:
            login = self._cli_man.input('Enter you GitHub login: ')
        if repo_name is None:
            repo_name = self._cli_man.input('Enter your repo name: ')
        command = f'git clone git@github.com:{login}/{repo_name}.git'
        print(f'Execute: {command}')
        os.system(f'git clone git@github.com:{login}/{repo_name}.git')
        self._cli_man.printer.smart.echo()
        self._cli_man.to_continue()

    def open_help(self):
        while True:
            self._cli_man.printer.smart.echo('Help:', '=')
            print('Configuring GitHub over SSH:')
            self._cli_man.printer.smart.echo()
            msg = 'g: generating new ssh key.\n'
            msg += 's: show and copying ssh key.\n'
            msg += 'a: adding ssh key to your GitHub account.\n'
            msg += 't: testing the ssh key (Testing the connection).\n'
            msg += 'c: cloning repositories.\n'
            msg += 'b: back to main menu.'
            print(msg)
            self._cli_man.printer.smart.echo()
            char = click.getchar()

            if char in ('b', 'и'):
                print('Help url: https://github.com/smartlegionlab/github-ssh-key')
                break

            if char in ('g', 'п'):
                self._new_help()
            elif char in ('s', 'ы'):
                self._copy_help()
            elif char in ('a', 'ф'):
                self._add_help()
            elif char in ('t', 'е'):
                self._test_help()
            elif char in ('c', 'с'):
                self._clone_help()
            else:
                continue
            self._cli_man.printer.smart.echo()

    def _new_help(self):
        self._cli_man.printer.smart.echo('Generating new ssh key:', '=')
        msg = '- Install openssh, or make sure you have it installed with the ssh command.\n'
        msg += '- During the generation process, enter your email that you use when working with GitHub.\n'
        msg += '- Do not change the default file name.\n'
        msg += "- Don't set a passphrase if you don't want to enter it every time."
        print(msg)
        self._cli_man.printer.smart.echo()
        if self._cli_man.get_action('Create new key?'):
            self.new_key()

    def _copy_help(self):
        self._cli_man.printer.smart.echo('Copying ssh key:', '=')
        print('- Highlight and completely copy your ssh key.')
        self._cli_man.printer.smart.echo()
        if self._cli_man.get_action('Show key?'):
            self.show_key()

    def _add_help(self):
        self._cli_man.printer.smart.echo('Adding ssh key to your GitHub account:', '=')
        print('- Highlight and completely copy your ssh key.')
        print('- Add your ssh key to your GitHub account.')
        self._cli_man.printer.smart.echo()
        if self._cli_man.get_action('Add key to your GitHub account?'):
            self.add_key()

    def _test_help(self):
        self._cli_man.printer.smart.echo('Testing the ssh key (Testing the connection):', '=')
        msg = 'For a successful connection, you had to follow these steps:\n\n'
        msg += '- Generate ssh key.\n'
        msg += '- Highlight and completely copy your ssh key.\n'
        msg += '- Add ssh key to your GitHub account.\n\n'
        msg += 'If you did everything correctly, you will see a personalized greeting.'
        print(msg)
        self._cli_man.printer.smart.echo()
        if self._cli_man.get_action('Test the key?'):
            self.test_key()

    def _clone_help(self):
        self._cli_man.printer.smart.echo('Cloning repositories:', '=')
        msg = 'To clone repositories, make sure:\n\n'
        msg += '- git installed.\n'
        msg += '- ssh key is generated and has a default name.\n'
        msg += '- the ssh key has been added to your GitHub account.\n'
        msg += '- when you test the connection, you see a personalized greeting.'
        print(msg)
        self._cli_man.printer.smart.echo()
        print('When cloning, the command will be used:')
        print('git clone git@github.com:[GitHub login]/[Repository name]')
        self._cli_man.printer.smart.echo()
        if self._cli_man.get_action('Clone repository?'):
            self.clone_repo()

    @staticmethod
    def _get_key():
        path = f'{Path.home()}/.ssh/id_ed25519.pub'
        if Path(path).exists():
            with open(f'{Path.home()}/.ssh/id_ed25519.pub', 'r') as f:
                text = f.read()
                return text
        return False
