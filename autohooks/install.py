# Copyright (C) 2017-2019 Greenbone Networks GmbH
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import shutil

from setuptools.command.install import install

from .utils import get_git_hook_directory_path, get_setup_directory_path


def get_pre_commit_hook_path():
    git_hook_dir_path = get_git_hook_directory_path()
    return git_hook_dir_path / 'pre-commit'


def get_pre_commit_hook_py_path():
    setup_dir_path = get_setup_directory_path()
    return setup_dir_path / 'pre-commit.py'


def install_pre_commit_hook(pre_commit_hook_file, pre_commit_hook):
    shutil.copy(str(pre_commit_hook_file), str(pre_commit_hook))


class PostInstall(install):

    def run(self):
        install.run(self)
        self.post_install()

    def post_install(self):
        pre_commit_hook = get_pre_commit_hook_path()
        if pre_commit_hook.exists():
            print('pre-commit hook already installed')
        else:
            pre_commit_hook_py = get_pre_commit_hook_py_path()
            install_pre_commit_hook(pre_commit_hook_py, pre_commit_hook)

            print('pre-commit hook installed at {}'.format(
                str(pre_commit_hook)))
