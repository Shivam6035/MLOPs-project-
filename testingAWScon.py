import boto3

def test_aws_connection():
    try:
        # 1. Check who is actually logged in
        sts = boto3.client('sts')
        identity = sts.get_caller_identity()
        print(f"✅ Successfully authenticated as: {identity['Arn']}")

        # 2. Test S3 upload directly
        bucket_name = "my-model-mlopsproj773" # Replace with your actual bucket name
        test_file = "test_upload.txt"
        
        with open(test_file, "w") as f:
            f.write("This is a test upload to check permissions.")
            
        s3 = boto3.client('s3')
        s3.upload_file(test_file, bucket_name, test_file)
        print(f"✅ Successfully uploaded test file to {bucket_name}!")
        
    except Exception as e:
        print(f"❌ AWS Error: {e}")

if __name__ == "__main__":
    test_aws_connection()