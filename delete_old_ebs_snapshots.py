"""
Deleting snapshots which are older than N days using boto library
"""

from datetime import datetime, timedelta, timezone
import boto3

ec2 = boto3.resource('ec2')

# list all the snapshots with filter for owner
snapshots = ec2.snapshots.filter(OwnerIds=['self'])

# iterate through each snapshot object
for snapshot in snapshots:
    # will return the created date of snapshot
    start_time = snapshot.start_time
    # will return the 15 days older time
    delete_time = datetime.now(tz=timezone.utc) - timedelta(days=15)
    # if start_time is older than 15 days time it will delete the snapshot
    if delete_time > start_time:
        snapshot.delete()
        print("Snapshot with id is deleted: {}", snapshot.snapshot_id)
    else:
        print(start_time)
        print("Snapshot with id : {} is not older than 15 days".format(snapshot.snapshot_id))
