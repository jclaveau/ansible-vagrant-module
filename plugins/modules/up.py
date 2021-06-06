#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, [Jean Claveau (https://github.com/jclaveau/ansible-vagrant-module)]
# Copyright: (c) 2017, [Tomas Kadlec (https://github.com/majidaldo/ansible-vagrant/commits?author=tomaskadlec)]
# Copyright: (c) 2015, [Majid alDosari (https://github.com/majidaldo/ansible-vagrant)]
# Copyright: (c) 2015, [caljess599 (https://github.com/caljess599/ansible-vagrant)]
# Copyright: (c) 2014, [Rob Parrot (https://github.com/robparrott/ansible-vagrant)]
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
# https://docs.ansible.com/ansible/2.10/dev_guide/testing/sanity/future-import-boilerplate.html
# https://docs.ansible.com/ansible/2.10/dev_guide/testing/sanity/metaclass-boilerplate.html

MAN = '''
Usage: vagrant up [options] [name|id]

Options:

        --[no-]provision             Enable or disable provisioning
        --provision-with x,y,z       Enable only certain provisioners, by type or by name.
        --[no-]destroy-on-error      Destroy machine if any fatal error happens (default to true)
        --[no-]parallel              Enable or disable parallelism if provider supports it
        --provider PROVIDER          Back the machine with a specific provider
        --[no-]install-provider      If possible, install the provider if it isn't installed
    -h, --help                       Print this help
'''

DOCUMENTATION = '''
---
module: jclaveau.vagrant.up
short_description: vagrant up for Ansible
description:
     - vagrant up for Ansible
version_added: "0.0.1"
author:
    - "Jean Claveau (@jclaveau)"
options:
  names:
    description:
      - names of the VMs to start
    type: list
    required: false
    default: []
  provision:
    description:
      - Enable or disable provisioning
    type: bool
    required: false
    default: []
  log:
    description:
      - Whether or not Vagrant's logs must be stored
    type: bool
    default: false
  vagrant_root:
    description:
      - the folder where vagrant files will be stored
    type: str
    default: .
  provider:
    default: virtualbox
    type: str
    description:
      - a provider to use instead of default virtualbox
requirements: ["vagrant, lockfile"]
'''


EXAMPLES = '''
- name: Spawn a new VM instance
  jclaveau.vagrant.up:
    names:
      - vm_name
'''

import sys
import subprocess
import os.path
# import json
# import ast
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.basic import missing_required_lib  # https://docs.ansible.com/ansible-core/devel/dev_guide/testing/sanity/import.html
import traceback
# import fcntl
# from io import StringIO
from ansible_collections.jclaveau.vagrant.plugins.module_utils.constants import *
from ansible_collections.jclaveau.vagrant.plugins.module_utils.VagrantWrapper import VagrantWrapper

try:
    import vagrant
except ImportError:
    HAS_VAGRANT_LIBRARY = False
    VAGRANT_LIBRARY_IMPORT_ERROR = traceback.format_exc()
else:
    HAS_VAGRANT_LIBRARY = True

# --------
# MAIN
# --------
def main():

    module = AnsibleModule(
        argument_spec=dict(
            vagrant_root=dict(default=DEFAULT_ROOT),
            name=dict(type='str'),
            provider=dict(default=DEFAULT_PROVIDER),
            parallel=dict(default=False, type='bool'),
            provision=dict(default=True, type='bool'),
            # provision_with=dict(default=[], type='list'),
        )
    )

    vagrant_root = module.params.get('vagrant_root')
    name = module.params.get('name')
    provider = module.params.get('provider')
    no_provision = not module.params.get('provision')
    # provision_with = module.params.get('provision_with')
    parallel = module.params.get('parallel')

    # --[no-]destroy-on-error      Destroy machine if any fatal error happens (default to true)
    # --[no-]install-provider      If possible, install the provider if it isn't installed

    vgw = VagrantWrapper(
        module=module,
        root_path=vagrant_root,
    )

    (changed, duration, status_before, status_after) = vgw.up(
        provider=provider,
        name=name,
        no_provision=no_provision,
        # provision_with=provision_with,
        parallel=parallel
    )

    module.exit_json(
      changed=changed,
      duration=duration,
      status_before=status_before,
      status_after=status_after,
      stdout_lines=list(vgw.stdout()),
      stderr_lines=list(vgw.stderr())
    )


main()
