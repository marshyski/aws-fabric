#!/usr/bin/python
# Get all running instances with a private IP in AWS VPC, exclude EMR nodes 

import boto.ec2.connection
import sys
import configuration as config

emr_tag = 'aws:elasticmapreduce:instance-group-role'

ec2 = boto.ec2.connect_to_region(config.AWS_REGIONS,
				aws_access_key_id=config.ACCESS_KEY,
				aws_secret_access_key=config.SECRET_KEY)

temp = sys.stdout
sys.stdout = open('hosts_file', 'w')
reservations = ec2.get_all_instances()
for res in reservations:
  for inst in res.instances:
    if inst.private_ip_address:
      if inst.state == 'running':
        if emr_tag in inst.tags:
	  pass
	else:
          print inst.private_ip_address
ec2.close()
sys.stdout.close()
sys.stdout = temp
