import boto3
import sys
from botocore.exceptions import ClientError

def list_storagegrid_bucket(endpoint_url, access_key, secret_key, bucket_name):
    """
    List contents of a StorageGRID bucket using boto3
    
    Parameters:
    endpoint_url (str): StorageGRID endpoint URL
    access_key (str): S3 access key
    secret_key (str): S3 secret key
    bucket_name (str): Name of the bucket to list
    """
    try:
        # Create an S3 client configured for StorageGRID
        s3_client = boto3.client(
            's3',
            endpoint_url=endpoint_url,
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            # Verify SSL certificates if your StorageGRID uses valid certs
            verify=True
        )
        
        print(f"\nListing contents of bucket: {bucket_name}\n")
        
        # List objects in the bucket with pagination
        paginator = s3_client.get_paginator('list_objects_v2')
        page_iterator = paginator.paginate(Bucket=bucket_name)
        
        for page in page_iterator:
            if 'Contents' in page:
                for obj in page['Contents']:
                    print(f"Key: {obj['Key']}")
                    print(f"Size: {obj['Size']} bytes")
                    print(f"Last Modified: {obj['LastModified']}")
                    print(f"Storage Class: {obj.get('StorageClass', 'STANDARD')}")
                    print("-" * 50)
            else:
                print("Bucket is empty")
                
        # Get bucket details
        bucket_details = s3_client.head_bucket(Bucket=bucket_name)
        print("\nBucket Details:")
        print(f"Request ID: {bucket_details['ResponseMetadata']['RequestId']}")
        
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == '404':
            print(f"Error: Bucket {bucket_name} does not exist")
        elif error_code == '403':
            print("Error: Access denied - check your credentials")
        else:
            print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Replace these values with your StorageGRID configuration
    ENDPOINT_URL = "https://s3.your-storagegrid-domain.com"
    ACCESS_KEY = "your_access_key"
    SECRET_KEY = "your_secret_key"
    BUCKET_NAME = "your-bucket-name"
    
    list_storagegrid_bucket(ENDPOINT_URL, ACCESS_KEY, SECRET_KEY, BUCKET_NAME)
