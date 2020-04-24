# snapshotalyzer-30000

Demo project to manange AWS EC@ instance snapshots

## About

This project is a demo, and uses boto3 to manage AWS EC2 instance snapshots

## Configuring

shotty uses the configuration file created by the AWS CLI e.g

 aws configure --profile shotty

## Running

 pipenv run python shotty/shotty.py <command> <--project=PROJECT>

 *command* is instances, volumes, snapshots
 *subcommab* is list, start or stop instances
 *project* is optional
