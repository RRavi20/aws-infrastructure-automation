import boto3

ec2 = boto3.resource('ec2', region_name="us-east-1")

def cleanup():
    # Find instances with our specific tag
    instances = ec2.instances.filter(
        Filters=[{'Name': 'tag:Name', 'Values': ['Automation-Project-Server']}]
    )
    
    for instance in instances:
        print(f"Terminating instance: {instance.id}")
        instance.terminate()
        print("Termination signal sent.")

if __name__ == "__main__":
    cleanup()