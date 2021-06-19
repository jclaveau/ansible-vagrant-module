# Repository [! MIGRATED HERE](https://github.com/jclaveau/ansible-vagrant-modules)

[![Sanity Tests](https://github.com/jclaveau/ansible-vagrant-modules/actions/workflows/sanity-tests.yaml/badge.svg?branch=main)](https://github.com/jclaveau/ansible-vagrant-modules/actions/workflows/sanity-tests.yaml?query=branch%3Amain)
[![Integration Tests](https://github.com/jclaveau/ansible-vagrant-modules/actions/workflows/integration-tests.yaml/badge.svg?branch=main)](https://github.com/jclaveau/ansible-vagrant-modules/actions/workflows/integration-tests.yaml?query=branch%3Amain)
[![Coverage](https://codecov.io/gh/jclaveau/ansible-vagrant-modules/branch/main/graph/badge.svg?token=qlZsPUMdwP)](https://app.codecov.io/gh/jclaveau/ansible-vagrant-modules/branch/main)

## Ansible Collection - [jclaveau.vagrant](https://github.com/jclaveau/ansible-vagrant-modules) LEGACY / ARCHIVED
This repo was a fork, from https://github.com/majidaldo/ansible-vagrant / https://github.com/robparrott/ansible-vagrant merged with https://github.com/bertvv/ansible-skeleton, which diverged so much than no PR would have sens anymore.

To fit Ansible's modules/collection guidelines and become maintainable on a long term it has been fully rewritten, the scope has been redefined (some out of scope features have been removed, others has been added), and the Vagrantfile handling fully refactored.

A new dedicated repo has been created in consequence: [jclaveau.vagrant](https://github.com/jclaveau/ansible-vagrant-modules)

### Credits

#### 2014 - [Rob Parrot](https://github.com/robparrott/ansible-vagrant)
* initial working poc
#### 2015 - [caljess599](https://github.com/caljess599/ansible-vagrant)
* modified Vagrantfile output to use API version 2
* disabled synced folders on all VMs created by Vagrantfile
* specified that forwarded port # specified on guest will be forwarded on host to 10000+# (e.g., guest: 80, host: 10080)
* added VAGRANT_ROOT variable to control where script-generated files are placed, update paths accordingly
* passed in vm_name without relying on argument order; changed status variable definition so 'if not running' check works
* changed count logic so if count on inventory is 1, doesn't change the vm name
* added logic to check if box image has changed
* repaired prepare_box logic to check if base image is already downloaded

#### 2015 - [Majid alDosari](https://github.com/majidaldo/ansible-vagrant)
* added log file. log: true|false
* added share_folder and share_mount nfs sharing (see module documentation)
* added config_code. custom configuation code that goes in the vagrantfile. the word config. will be converted to config_"machine" so that you can have machine-specific options. great for hypervisor options such as config.vm.memory ...

#### 2017 - [Tomas Kadlec](https://github.com/majidaldo/ansible-vagrant/commits?author=tomaskadlec)
* added provider option, default value is virtualbox

#### 2017 - 2020 Thanks, to the team of [Ansible Skeleton](https://github.com/bertvv/ansible-skeleton) for their really smart work
- [Bert Van Vreckem](https://github.com/bertvv/) (maintainer)
- [Brian Stewart](https://github.com/thecodesmith)
- [Jeroen De Meerleer](https://github.com/JeroenED)
- [Mathias Stadler](https://github.com/MathiasStadler)

#### 2021 - [Jean Claveau](https://github.com/jclaveau/ansible-vagrant-module)
* integrate `ansible-test` and setup CI with github actions
* integration tests and sanity tests
* Python 3 support
* replace the json and lock parts by integrating Vagrantfile driven by Yaml from [ansible-skeleton](https://github.com/bertvv/ansible-skeleton)
* full rewrite to reduce the code responsability thus improve it's maintainability: one module per vagrant command.
  A lot of the previous work has been suppressed here but it has been a huge source of inspiration for a nice workflow.
* vagrant stdout and stderr made available in ansible results
* rewrite simplified docs
* adding some missing Vagrant commands: suspend, resume, port, reload, ssh
* multi-provisionning support
