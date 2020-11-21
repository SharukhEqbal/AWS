# Operations on EC2 Start, Stop and terminate
import boto3

# it will create an ec2 instance
client = boto3.client('ec2')

# start an instance will take InstanceIds as required parameter,
# other parameters are optional
client.start_instances(InstanceIds=['i-XXXX'])
print('The instance is started')

# To stop the instance
response = client.stop_instances(InstanceIds=['i-XXXX'])
print('The instance is stopped')
for instance in response['StoppingInstances']:
    print(instance['InstanceId'])

# To terminate the instance
response = client.terminate_instances(InstanceIds=['i-XXXX'])

# To get the instance id of the terminated instance from Response data
for instance in response['TerminatingInstances']:
    print("The instance id terminated {}".format(instance['InstanceId']))
