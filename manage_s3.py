import boto3
import random
import string

def create_automated_bucket(region="us-east-1"):
    s3 = boto3.client('s3', region_name=region)
    
    # Generate a unique name
    suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    bucket_name = f"bca-project-storage-{suffix}"
    
    print(f"Creating bucket: {bucket_name}...")
    
    try:
        s3.create_bucket(Bucket=bucket_name)
        print(f"Success! Bucket '{bucket_name}' is ready.")
        
        # Upload a test file to the bucket
        with open("log.txt", "w") as f:
            f.write("Infrastructure provisioned successfully.")
            
        s3.upload_file("log.txt", bucket_name, "setup_log.txt")
        print("Initial log file uploaded to S3.")
        
    except Exception as e:
        print(f"S3 Error: {e}")

if __name__ == "__main__":
    create_automated_bucket()