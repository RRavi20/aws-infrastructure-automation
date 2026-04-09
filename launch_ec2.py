import boto3

# 1. Configuration 
MY_REGION = "us-east-1"
MY_KEY_PAIR = "MyWindowsKey"  
# Try this updated AMI ID for Amazon Linux 2023 in us-east-1
MY_AMI = "ami-0440d3b780d96b29d" 

def launch_instance():
    ec2 = boto3.resource('ec2', region_name=MY_REGION)
    print(f"Attempting to launch instance in {MY_REGION}...")

    try:
        instances = ec2.create_instances(
            ImageId=MY_AMI.strip(), # .strip() removes accidental spaces
            MinCount=1,
            MaxCount=1,
            InstanceType='t2.micro',
            KeyName=MY_KEY_PAIR
        )
        
        new_instance = instances[0]
        print(f"Success! Instance ID: {new_instance.id}")
        
        print("Waiting for instance to initialize...")
        new_instance.wait_until_exists()
        
        new_instance.create_tags(Tags=[{'Key': 'Name', 'Value': 'Automation-Project-Server'}])
        print("Instance tagged successfully!")

    except Exception as e:
        print(f"Error during launch: {e}")

if __name__ == "__main__":
    launch_instance()