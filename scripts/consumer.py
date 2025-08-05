import boto3
import time
import json

# Correct region
sqs = boto3.client('sqs', region_name='eu-north-1')

# Get queue URL
queue_name = 'FairQueueDemo'
queue_url = sqs.get_queue_url(QueueName=queue_name)['QueueUrl']
print(f"Connected to queue: {queue_name} in eu-north-1")

# Start polling
while True:
    print("Polling for messages...")
    try:
        response = sqs.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=5,
            MessageAttributeNames=['All'],
            WaitTimeSeconds=5
        )

        if 'Messages' not in response:
            print("No messages found.")
            time.sleep(1)
            continue

        messages = response['Messages']
        print(f"Received {len(messages)} messages")

        for msg in messages:
            print("Raw message:", json.dumps(msg, indent=2))

            tenant_attr = msg.get('MessageAttributes', {}).get('Tenant', {})
            tenant = tenant_attr.get('StringValue', 'Unknown')

            print(f"Processing: {msg['Body']} from {tenant}")

            sqs.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=msg['ReceiptHandle']
            )
            print("Deleted message")

    except Exception as e:
        print(f"Error: {str(e)}")
        time.sleep(2)
