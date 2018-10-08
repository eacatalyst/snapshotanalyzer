# snapshotanalyzer

Demo project to manage AWS EC2 instances snapshots

## About

This project is a demo, and uses boto3 to manage AWS EC2 instance snapshots

## Configuring

shotty uses the configuration file created by the AWS cli. e.g.

'aws configure --profile shotty'

## Running

'pipenv run "python shotty/shotty.py"'

## Fix Issues with pipenv on Ubuntu
https://github.com/pypa/pipenv/issues/2924

pip install --user git+https://github.com/pypa/pipenv.git
