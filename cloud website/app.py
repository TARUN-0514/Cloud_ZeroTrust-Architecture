import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        # Print the entire event for reference
        print("Received event: " + json.dumps(event, indent=2))

        # Extract the object key from the event
        object_key = event['Records'][0]['s3']['object']['key']

        # Specify the source and destination bucket names
        src_bucket = event['Records'][0]['s3']['bucket']['name']
        dest_bucket = 'website-cloud-s3'  # Replace with your destination bucket name
        dest_folder = 'uploded-files/'       # Replace with your desired folder

        # Specify the destination key (object key)
        dest_key = dest_folder + object_key

        # Copy the file from the source to the destination
        s3.copy_object(
            Bucket=dest_bucket,
            CopySource={'Bucket': src_bucket, 'Key': object_key},
            Key=dest_key
        )

        print(f"File copied from {src_bucket}/{object_key} to {dest_bucket}/{dest_key}")
    except Exception as e:
        print(f"Error: {str(e)}")
        raise e
