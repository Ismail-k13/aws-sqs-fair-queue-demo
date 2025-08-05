import boto3
import random
import time

sqs = boto3.client('sqs', region_name='eu-north-1')
queue_url = sqs.get_queue_url(QueueName='FairQueueDemo')['QueueUrl']

tenants = ['TenantA', 'TenantB', 'TenantC']

for _ in range(10):
    tenant = random.choice(tenants)
    message_body = f'{tenant} message'

    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=message_body,
        MessageAttributes={
            'Tenant': {
                'StringValue': tenant,
                'DataType': 'String'
            }
        }
    )

    print(f"Sent: {message_body}")
    time.sleep(0.5)
