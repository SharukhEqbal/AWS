# pip install boto3
import boto3

# will connect to boto3 client
client = boto3.client('ec2')
print(client)
# launch an EC2 Instance
response = client.run_instances(ImageId='ami-XXXXX',
                     InstanceType='t2.micro',
                     MinCount=1,
                     MaxCount=1)

# response result is in dict filtering out the instanceId
for instance in response['Instances']:
    print(instance['InstanceId'])

