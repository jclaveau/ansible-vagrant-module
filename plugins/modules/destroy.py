#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, [Jean Claveau (https://github.com/jclaveau/ansible-vagrant-module)]
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
# https://docs.ansible.com/ansible/2.10/dev_guide/testing/sanity/future-import-boilerplate.html
# https://docs.ansible.com/ansible/2.10/dev_guide/testing/sanity/metaclass-boilerplate.html

MAN = '''
Usage: vagrant destroy [options] [name|id]

Options:

    -f, --force                      Destroy without confirmation.
        --[no-]parallel              Enable or disable parallelism if provider supports it (automatically enables force)
    -h, --help                       Print this help
'''

DOCUMENTATION = '''
---
module: jclaveau.vagrant.destroy
short_description: vagrant destroy of only one vm
description:
     - vagrant destroy of one vm
version_added: "0.0.1"
author:
    - "Jean Claveau (@jclaveau)"
options:
  name:
    description:
      - name of the VM to start
    type: str
  vagrant_root:
    description:
      - the folder where vagrant files will be stored
    type: str
    default: .
requirements: ["vagrant"]
'''

EXAMPLES = '''
- name: Spawn a new VM instance
  jclaveau.vagrant.destroy:
    name: vm_name
    force: true
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.basic import missing_required_lib  # https://docs.ansible.com/ansible-core/devel/dev_guide/testing/sanity/import.html

from ansible_collections.jclaveau.vagrant.plugins.module_utils.constants import *
from ansible_collections.jclaveau.vagrant.plugins.module_utils.VagrantWrapper import VagrantWrapper


# --------
# MAIN
# --------
def main():

    module = AnsibleModule(
        argument_spec=dict(
            vagrant_root=dict(default=DEFAULT_ROOT),
            name=dict(type='str'),
        )
    )

    vagrant_root = module.params.get('vagrant_root')
    name = module.params.get('name')

    vgw = VagrantWrapper(
        module=module,
        root_path=vagrant_root,
    )

    (changed, duration, status_before, status_after) = vgw.destroy(
        name=name
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
