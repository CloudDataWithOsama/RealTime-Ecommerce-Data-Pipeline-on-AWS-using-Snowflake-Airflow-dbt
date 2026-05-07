# EC2 + Kinesis + S3 Setup Commands

sudo yum update -y

sudo yum install -y aws-kinesis-agent

sudo nano /etc/aws-kinesis/agent.json

sudo service aws-kinesis-agent start

sudo chkconfig aws-kinesis-agent on

sudo chmod 777 /tmp

sudo yum install python3 -y

sudo yum install python3-pip -y

pip3 install Faker

nano simulation.py

python3 simulation.py