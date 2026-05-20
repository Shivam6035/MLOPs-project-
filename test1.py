# will show all avaliable buckets in your AWS account

import boto3

def list_my_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    
    print("Buckets in your AWS account:")
    for bucket in response.get('Buckets', []):
        print(f" - {bucket['Name']}")

if __name__ == "__main__":
    list_my_buckets()