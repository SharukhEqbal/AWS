"""
Create a image wait for the image to be available and then copy it to another region
"""
import boto3

source_region = 'ap-south-1'
# getting ec2 instance in ap-south-1 region
ec2 = boto3.resource('ec2', region_name=source_region)

# using collections to get instances and then filter with it's instance_id
instances = ec2.instances.filter(InstanceIds=['i-0f73bc3ae18d4b8ce'])

image_ids = []

for instance in instances:
    # creating image by passing parameter Name and Description
    image = instance.create_image(Name='First Image for - '+instance.id, Description='Image from boto for '+instance.id)
    # this image ids will be used to copy it to another region
    image_ids.append(image.id)

print("Images to be copied: {}".format(image_ids))

# wait for the image to be available
# image creation is done asynchronously and takes around 1-2 min

client = boto3.client('ec2', region_name=source_region)
# different waiters are available we are going to use image_available waiter
waiter = client.get_waiter('image_available')

# wait for the image to be available
waiter.wait(Filters=[{
    'Name': 'image-id',
    'Values': image_ids
}])


# copy images to another region

destination_region = 'us-east-1'
client = boto3.client('ec2', region_name=destination_region)
for image_id in image_ids:
    client.copy_image(Name='CopiedImageFromMumbaiRegion', SourceImageId=image_id, SourceRegion=source_region)
