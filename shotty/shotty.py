import boto3
import sys
import click

session = boto3.Session(profile_name='shotty')
ec2 = session.resource('ec2')

@click.command()
def list_instances():
    "List EC2 Instances"
    for i in  ec2.instances.all():
        print(', '.join((
           i.id,
           i.instance_type,
           i.placement['AvailabilityZone'],
           i.state['Name'],
           i.public_dns_name)))

    return

if __name__ == '__main__':
    list_instances()


# shotty list instances
# shotty instances list
# shotty snapshot instances
# shotty instances shapshot
# shotty instances create-snapshots
# shotty list volumes
# shotty volumes list_instances
# shotty instances stop tag=Project:valkyre
# shotty start instances --project=valkyre
# shotty instances stop
