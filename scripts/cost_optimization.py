import boto3

def terminate_idle_instances():
    ec2 = boto3.client('ec2')
    instances = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            if instance['State']['Name'] == 'running' and is_idle(instance):
                ec2.terminate_instances(InstanceIds=[instance['InstanceId']])
                print(f"Terminated instance: {instance['InstanceId']}")

def is_idle(instance):
    # Placeholder for actual idle check logic
    return True

if __name__ == "__main__":
    terminate_idle_instances()