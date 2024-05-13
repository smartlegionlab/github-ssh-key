# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
from github_ssh_key import __version__
from smartcliapp import Informer

from github_ssh_key.commander import Commander


class CliManager(Informer):
    commander = Commander()
    name = "github-ssh-key"
    title = "Smart Legion Lab"
    description = "Github Ssh Key Manager"
    url = "https://github.com/smartlegionlab"
    copyright = "Copyright © 2018-2024, A.A Suvorov"
    version = __version__
