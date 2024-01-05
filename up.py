import boto3

from save import quotes_json

client = boto3.client('lambda', region_name='eu-central-1')

response = client.invoke(
  FunctionName='my-function-name',
  Payload=quotes_json
)

print(response)