# -*- coding: utf-8 -*-

# Copyright: (c) 2017, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class ModuleDocFragment(object):

    # Documentation fragment for ProxySQL connectivity
    CONNECTIVITY = r'''
options:
  login_user:
    description:
      - The username used to authenticate to ProxySQL admin interface.
    type: str
  login_password:
    description:
      - The password used to authenticate to ProxySQL admin interface.
    type: str
  login_host:
    description:
      - The host used to connect to ProxySQL admin interface.
    type: str
    default: '127.0.0.1'
  login_unix_socket:
    description:
      - The socket used to connect to ProxySQL admin interface.
    type: str
  login_port:
    description:
      - The port used to connect to ProxySQL admin interface.
    type: int
    default: 6032
  config_file:
    description:
      - Specify a config file from which I(login_user) and I(login_password)
        are to be read.
    type: path
    default: ''
requirements:
   - PyMySQL
   - mysqlclient
'''

    # Documentation fragment for managing ProxySQL configuration
    MANAGING_CONFIG = r'''
options:
  save_to_disk:
    description:
      - Save config to sqlite db on disk to persist the configuration.
    type: bool
    default: true
  load_to_runtime:
    description:
      - Dynamically load config to runtime memory.
    type: bool
    default: true
'''

    # Standard attribute descriptions. Each module sets its own support level.
    ATTRIBUTES = r'''
options: {}
attributes:
  check_mode:
    description:
      - Can run in check mode and return changed status prediction without modifying the target.
  idempotent:
    description:
      - When run twice in a row outside check mode, with the same arguments, the second invocation indicates no change.
      - This assumes that the system controlled/queried by the module has not changed in a relevant way.
'''

    # For modules that never modify state, such as info modules
    IDEMPOTENT_NOT_MODIFY_STATE = r'''
options: {}
attributes:
  idempotent:
    support: full
    details:
      - This action does not modify state.
'''
