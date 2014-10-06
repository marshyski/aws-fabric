aws-fabric
==========

RHEL/CentOS/Fedora [Python Fabric][1] script to manage AWS fleet

Requirements
------------
  * root or equivalent
  * Amazon Web Services (AWS) account
  * Python 2.6/7
  * Python pip
  * Python fabric, boto, botocore

**Getting started with [aws-fabric][2]:**

    git clone https://github.com/marshyski/aws-fabric.git
    cd aws-fabric && pip install -r requirements.txt
    
    #Edit variables in configuration.py:
    ACCESS_KEY = 'aws-access-key-here'
    SECRET_KEY = 'aws-secret-key-here'
    KEY_FILE = '~/.ssh/keypair.pem'
    USERNAME = 'ec2-user'
    AWS_REGIONS = 'us-east-1'
    
    #Verify EMR tag (leave value if not using EMR) in instances.py:
    emr_tag = 'aws:elasticmapreduce:instance-group-role'


    fab -l #Output:
    clean_up
    gem_install
    gem_update
    install_base
    install_docker
    install_epel
    install_python
    pip_install
    pip_upgrade
    provision_box
    update_system
    yum_install
    yum_remove

    # Only run when AWS instance is up
    fab provision_box
    # yum install example
    fab yum_install:httpd
    # pip install example
    fab pip_install:flask


  [1]: http://fabfile.org/
  [2]: https://github.com/marshyski/aws-fabric
