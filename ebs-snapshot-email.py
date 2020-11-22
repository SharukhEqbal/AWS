"""
Create a snapshot and then send the snapshot_ids in the emails
"""
import boto3

ec2 = boto3.resource('ec2')
sns_client = boto3.client('sns')

# filter instances based on backup tag value of instance
backup_filter = [
    {
        'Name': 'tag:Backup',
        'Values': ['Yes']
    }
]

snapshot_ids = []

# List all the ec2 instances based on the filter
for instance in ec2.instances.filter(Filters=backup_filter):
    # list all the volumes attached to the instance
    for vol in instance.volumes.all():
        # Create a snapshot of the volume
        snapshot = vol.create_snapshot(Description='Snapshot created by boto3')
        snapshot_ids.append(snapshot.snapshot_id)

# publishing the details to the topic which in turns send email notification to the subscriber
sns_client.publish(
    TopicArn = 'arn:aws:sns:ap-south-1:075189002919:Boto3SNS',
    Subject = 'EBS Snapshot',
    Message = str(snapshot_ids)
)