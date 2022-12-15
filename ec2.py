import json
import boto3

client = boto3.client('ec2')

instances_ids = []

cloudwatch_input = "start"

all_ec2_instances = client.describe_instances(
    Filters = [
    {
        'Name':'tag:liga',
        'Values':["true"]
    }
]
) if cloudwatch_input == "start" else client.describe_instances()

instances_full_details = all_ec2_instances['Reservations']

instance_ids = []

for instance_detail in instances_full_details:
    group_instances = instance_detail['Instances']

    for instance in group_instances:
        instance_ids.append(instance['InstanceId'])

print(instance_ids)