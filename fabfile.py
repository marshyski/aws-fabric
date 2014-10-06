#!/usr/bin/python
#This fabric script must be used with `RHEL/CentOS/Fedora` systems

from fabric.api import sudo, run, env, cd
import sys
import os
import configuration as config
import instances

if os.stat('hosts_file').st_size == 0:
  print "hosts_file is empty\n"
  sys.exit(1)

env.hosts = open('hosts_file', 'r').readlines()
env.user = config.USERNAME
env.port = '22'
env.key_filename = config.KEY_FILE
env.warn_only = True

#Run this for the first time on a box to set it up
def provision_box():
    update_system()
    install_epel()
    install_base()
    install_python27()
    clean_up()

#Update system via yum
def update_system():
    sudo('yum update --nogpgcheck --skip-broken -y update')    

#Install EPEL repo file
def install_epel():
    sudo('yum install --nogpgcheck -y http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm')

#Install packages defined below
def yum_install(*packages):
    sudo('yum install --nogpgcheck --skip-broken -y %s' % ' '.join(packages), shell=False)

#Remove packages defined below
def yum_remove(*packages):
    sudo('yum remove -y --skip-broken %s' % ' '.join(packages), shell=False)

#Install dependencies on system via yum 
def install_base():
    yum_install('dos2unix glances screen gcc make python-devel python-setuptools python-pip git rubygems rpmbuild ruby-devel')

#Install Docker LXC Engine
def install_docker():
    yum_install('docker-io')
    sudo('/sbin/chkconfig docker on')
    sudo('/sbin/service docker start')

#Install Python pip packages
def pip_install(*pip):
    sudo('pip install %s' % ' '.join(pip), shell=False)

#Upgrade Python pip packages
def pip_upgrade(*pip):
    sudo('pip install --upgrade %s' % ' '.join(pip), shell=False)

#Install Ruby gems
def gem_install(*gem):
    sudo('gem install %s' % ' '.join(gem), shell=False)

#Update Ruby gem
def gem_update(*gem):
    sudo('gem update %s' % ' '.join(gem), shell=False)

#Install Python 2.7.8
def install_python():
    run('curl -O https://www.python.org/ftp/python/2.7.8/Python-2.7.8.tar.xz')
    run('tar xfv Python-2.7.8.tar.xz')
    with cd ('Python-2.7.8'):
        sudo('./configure --prefix=/usr/local --enable-unicode=ucs4 --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib"')
        sudo('make && make altinstall')

#Clean up yum/rpm & post-install of Python 2.7
def clean_up():
    yum_remove('gcc')
    sudo('rm -f /var/lib/rpm/__db*; rpm --rebuilddb')
    sudo('yum history new; yum clean all')
    sudo('rm -rf Python-*')
