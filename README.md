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

### ___github-ssh-key v0.1.4___

- Go to new version [smartcliapp](https://github.com/smartlegionlab/smartcliapp)

***

## Description:

___github-ssh-key___ - GitHub ssh key manager. Console utility for creating, getting, 
testing, using public ssh keys for GitHub.

Possibilities:

- Generating ssh keys for GitHub;
- Output ssh key to the console;
- Checking the ssh key, testing the connection;
- Interactive menu for working with the utility;
- Launch the default browser with a page for adding ssh key on GitHub;
- Cloning private repositories via ssh;


***

## Help:

### Install and use:

#### Install:

`pip3 install github-ssh-key`

#### Use:

`github-ssh-key`

To access GitHub over ssh, you should run some sequence of actions.

- Install openssh;
- Generate new ssh keys;
- Copy the public key;
- Add your public key to GitHub;
- Check the connection;
- Open page `https://github.com/settings/keys` in the default browser.

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

`github-ssh-key [command] -h`

`github-ssh-key run -h`
`github-ssh-key new -h`
`github-ssh-key show -h`
`github-ssh-key test -h`
`github-ssh-key clone -h`
`github-ssh-key github -h`


#### Commands:

`github-ssh-key [command] [args]`

- run `github-ssh-key run`
- new `github-ssh-key new -e [your email]`
- show `github-ssh-key show`
- test `github-ssh-key test`
- clone `github-ssh-key clone -l [GitHub login] -n [repo name]`
- github `github-ssh-key github`


#### Variant 1:

- Go to the project folder
- `python3 setup.py install`
- `github-ssh-key`
- `github-ssh-key -h`
- `github-ssh-key run`
- `github-ssh-key new -e [your email]`
- `github-ssh-key show`
- `github-ssh-key test`
- `github-ssh-key clone -l [your login from github] -n [github repository name for cloning]`


#### Variant 2:

- Install [python](https://python.org)
- Go to the project folder
- `pip3 install -r requirements.txt`
- `python3 github-ssh-key.py`
- `python3 github-ssh-key.py -h`
- `python3 github-ssh-key.py run`
- `python3 github-ssh-key.py new -e [your email]`
- `python3 github-ssh-key.py show`
- `python3 github-ssh-key.py test`
- `python3 github-ssh-key.py clone -l [your login from github] -n [github repository name for cloning]`

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
