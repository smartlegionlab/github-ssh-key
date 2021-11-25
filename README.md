# github-ssh-key

***

![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/github-ssh-key)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/github-ssh-key?label=pypi%20downloads)](https://pypi.org/project/github-ssh-key/)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/github-ssh-key)](https://github.com/smartlegionlab/github-ssh-key/)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/github-ssh-key)](https://github.com/smartlegionlab/github-ssh-key/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/github-ssh-key)](https://pypi.org/project/github-ssh-key)
[![PyPI - Format](https://img.shields.io/pypi/format/github-ssh-key)](https://pypi.org/project/github-ssh-key)
[![GitHub Repo stars](https://img.shields.io/github/stars/smartlegionlab/github-ssh-key?style=social)](https://github.com/smartlegionlab/github-ssh-key/)
[![GitHub watchers](https://img.shields.io/github/watchers/smartlegionlab/github-ssh-key?style=social)](https://github.com/smartlegionlab/github-ssh-key/)
[![GitHub forks](https://img.shields.io/github/forks/smartlegionlab/github-ssh-key?style=social)](https://github.com/smartlegionlab/github-ssh-key/)

***

## Short Description:
___github-ssh-key___ - GitHub ssh key manager. Console utility for creating, getting, testing, 
using public ssh keys for GitHub.

***

Author and developer: ___A.A Suvorov___

[![smartlegiondev@gmail.com](https://img.shields.io/static/v1?label=email:&message=smartlegiondev@gmail.com&color=blue)](mailto:smartlegiondev@gmail.com)

***

## Help the project financially:

- PayPal: [https://paypal.me/smartlegionlab](https://paypal.me/smartlegionlab)
- Yandex Money: [https://yoomoney.ru/to/4100115206129186](https://yoomoney.ru/to/4100115206129186)
- LiberaPay: [https://liberapay.com/smartlegion/donate](https://liberapay.com/smartlegion/donate)
- Visa: 4048 0250 0089 5923

***

## Supported:

- Linux: All.
- Termux (Android).

***

## Images:

![logo](https://github.com/smartlegionlab/github-ssh-key/raw/master/data/images/github-ssh-key.png)

***

## What's new?

### ___github-ssh-key v0.2.0___

- Fixed bugs.
- Added interactive help menu.
- Changed interface.
- Changed some commands.
- A more complete description of working with the utility and 
working with ssh keys in general has been added.

***

## Description:

___github-ssh-key___ - GitHub ssh key manager. Console utility for creating, getting, 
testing, using public ssh keys for GitHub.

Possibilities:

- Generating ssh keys for GitHub.
- Output ssh key to the console.
- Добавление ssh ключа на GitHub.
- Checking the ssh key, testing the connection.
- Interactive menu for working with the utility.
- Interactive menu for help.
- Launch the default browser with a page for adding ssh key on GitHub.
- Cloning private repositories via ssh.
- Running individual commands.

***

## Help:

### Install and use:

#### Install:

`pip3 install github-ssh-key`

`github-ssh-key`

#### Use:

To access GitHub over ssh, you should run some sequence of actions.

- Install openssh;
- Generate new ssh keys;
- Copy the public key;
- Add your public key to GitHub;
- Check the connection;

This utility provides you with these capabilities.

Adding a key to your GitHub account involves several steps:

1. Generating new ssh key.
   - Install openssh, or make sure you have it installed with the ssh command.
   - During the generation process, enter your email that you use when working with GitHub.
   - Do not change the default file name.
   - Don't set a passphrase if you don't want to enter it every time.
2. Copying ssh key.
   - Highlight and completely copy your ssh key.
3. Adding ssh key to your GitHub account.
   - Highlight and completely copy your ssh key.
   - Add your ssh key to your GitHub account.
4. Testing the ssh key (Testing the connection).
   - For a successful connection, you had to follow these steps:
     - Generate ssh key.
     - Highlight and completely copy your ssh key.
     - Add ssh key to your GitHub account.
     - If you did everything correctly, you will see a personalized greeting.

Also, directly from the interactive menu, you can clone your private
repository using ssh.

To get help with commands, use:

`github-ssh-key [command] -h`

`github-ssh-key new -h`
`github-ssh-key show -h`
`github-ssh-key add -h`
`github-ssh-key test -h`
`github-ssh-key clone -h`
`github-ssh-key help -h`

#### Commands:

`github-ssh-key [command] [args]`

- run `github-ssh-key run`
- new `github-ssh-key new -e [your email]`
- show `github-ssh-key show`
- add `github-ssh-key add`
- test `github-ssh-key test`
- clone `github-ssh-key clone -l [GitHub login] -n [repo name]`


#### Variant 1:

- Go to the project folder
- `python3 setup.py install`
- `github-ssh-key`

#### Variant 2:

- Install [python](https://python.org)
- Go to the project folder
- `pip3 install -r requirements.txt`
- `python3 github-ssh-key.py`

***

## Disclaimer of liability:

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

***

## Copyright:
    --------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details).
    Copyright © 2018-2021, A.A Suvorov
    All rights reserved.
    --------------------------------------------------------
