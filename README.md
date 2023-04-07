# tf_ansible_CassandraCluster
Deploy a Cassandra Cluster in AWS using Terraform, Ansible Playbook, and a python script

Terraform will set up the VPC, EC2 and other infrastructure for Cassandra to be deployed

The seeds_cassandra.py - will stip the trailing line off the string in the seeds file.  
The new string will be assigned to variable, and used to replace the '- seeds: "127.0.0.1:7000". in the cassandra.yaml

The Ansible Playbook "InstallCassandra" will install Cassandra on the VPC

I use the tarball for the installation, because Apt install will automatically start Cassandra. 
We want the Cassandra to start using the Ec2Snitch and the seeds ips, rpc_address, and listen_address,
that were assigned with in Terraform and with the python script.

Terraform will output the IP addresses of the EC2 machines.

You will have to ssh into each EC2 machine and start Cassandra from the cassandra/bin folder

After Cassandra has started run bin/nodetool status

The output should be similar as below:

Datacenter: us-west-2
=====================
Status=Up/Down
|/ State=Normal/Leaving/Joining/Moving
--  Address    Load       Tokens       Owns (effective)  Host ID                               Rack
UN  10.0.1.35  66.49 KiB  16           75.7%             033ed89e-1643-4b75-81c0-fba1ec03a5dd  2b
UN  10.0.0.29  66.49 KiB  16           61.6%             edbe09e7-b1f3-4dd3-933e-fc31f963f82b  2a
UN  10.0.2.29  66.49 KiB  16           62.7%             38122871-8129-459a-bf5f-eef53678f389  2c


*NOTE - I haven't yet figured out how to programmatically start Cassandra with Ansible
