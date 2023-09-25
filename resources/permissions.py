import boto3
import json

S3API = boto3.client("s3", region_name="us-east-1") 
bucket_name = "c81790a1735454l4825114t1w336573178886-s3bucket-1qrmrarpsbwiz"

policy_file = open("/home/ec2-user/environment/resources/public_policy.json", "r")


S3API.put_bucket_policy(
    Bucket = bucket_name,
    Policy = policy_file.read()
)
print ("Setting Permissions - DONE")