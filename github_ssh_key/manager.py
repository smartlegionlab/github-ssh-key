# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
from github_ssh_key import __version__
from smartcliapp.informers import Informer

from github_ssh_key.commander import Commander


class CliMan(Informer):
    commander = Commander()
    name = "github-ssh-key"
    title = "Smart Legion Lab"
    description = "Github Ssh Key Manager"
    url = "https://github.com/smartlegionlab"
    copyright = "Copyright © 2018-2021, A.A Suvorov"
    version = __version__
