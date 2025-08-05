# AWS SQS Fair Queue Demo - Complete Documentation

## Overview

This documentation provides a complete walkthrough of building and running a demo for Amazon SQS Fair Queues using Python, AWS Free Tier, and the Boto3 SDK. The goal of this project is to demonstrate how Fair Queues automatically ensure message delivery fairness among tenants without requiring application-level throttling or prioritization logic.

---

## Table of Contents

1. Introduction to SQS Fair Queues
2. Prerequisites
3. AWS Setup

   * IAM User Creation
   * Access Key and Secret Key
4. Creating the SQS Fair Queue
5. Local Environment Setup

   * Cloning the Repository
   * Installing Python Requirements
6. Understanding the Folder Structure
7. Code Explanation

   * Producer Script (`producer.py`)
   * Consumer Script (`consumer.py`)
8. Why Two Terminals Are Used
9. Running the Demo
10. Observing Results in AWS Console
11. Cleanup Steps and Security Best Practices
12. Conclusion

---

## 1. Introduction to SQS Fair Queues

Amazon SQS Fair Queues provide a new queue type that balances message consumption from different tenants or sources. Instead of relying on application logic to prevent noisy tenants from dominating the queue, Fair Queues apply adaptive rate-limiting and deliver messages fairly.

---

## 2. Prerequisites

Before starting the project, ensure you have the following:

* An AWS Free Tier account
* Python 3.8 or later
* AWS CLI installed and configured
* Git installed on your system
* A GitHub repository (e.g., [https://github.com/Ismail-k13/aws-sqs-fair-queue-demo.git](https://github.com/Ismail-k13/aws-sqs-fair-queue-demo.git))

---

## 3. AWS Setup

### IAM User Creation

You need to create an IAM user to interact with AWS services securely.

1. Go to the [AWS IAM Console](https://console.aws.amazon.com/iam/)
2. Click on "Users" > "Add user"
3. Enter a username (e.g., `sqs-fair-demo-user`)
4. Enable "Programmatic access"
5. Attach policies:

   * `AmazonSQSFullAccess`
6. Create the user and save the Access Key ID and Secret Access Key securely

### Why Access and Secret Keys Are Needed

These keys authenticate your local Python scripts with AWS to send/receive messages via the SQS service using the Boto3 SDK.

---

## 4. Creating the SQS Fair Queue

1. Go to the [Amazon SQS Console](https://console.aws.amazon.com/sqs/)
2. Click "Create Queue"
3. Select "Fair Queue"
4. Name the queue: `FairQueueDemo`
5. Region: `eu-north-1` (Stockholm) to stay within Free Tier
6. Click "Create Queue"

Note: Do it in your region.
---

## 5. Local Environment Setup

### Clone the Repository

```bash
git clone https://github.com/Ismail-k13/aws-sqs-fair-queue-demo.git
cd aws-sqs-fair-queue-demo
```

### Install Python Dependencies

```bash
pip install boto3
```

Add this to a file named `requirements.txt` if not already present:

```
boto3
```

---

## 6. Folder Structure

```text
aws-sqs-fair-queue-demo/
├── scripts/
│   ├── producer.py      # Sends messages from tenants
│   └── consumer.py      # Consumes and processes messages
├── assets/
│   └── screenshots/     # Optional visuals for queue setup and metrics
├── .gitignore
├── README.md
├── LICENSE
└── requirements.txt
```

---

## 7. Code Explanation

### producer.py

This script simulates sending messages from multiple tenants: `TenantA`, `TenantB`, and `TenantC`. TenantB sends more messages to simulate a noisy tenant.

It uses the `MessageAttributes` field to label each message with its tenant.

Command to run:

```bash
python scripts/producer.py
```

### consumer.py

This script polls the queue continuously and prints the messages it receives. It demonstrates how Fair Queues ensure fairness by balancing message delivery from each tenant.

Command to run:

```bash
python scripts/consumer.py
```

---

## 8. Why Two Terminals Are Used

Using separate terminals for producer and consumer scripts allows parallel simulation:

* One terminal runs `producer.py` to continuously send messages
* Another runs `consumer.py` to poll and process messages

This setup helps observe real-time fairness behavior, especially when one tenant is sending more messages.

---

## 9. Running the Demo

1. Open Terminal 1:

```bash
python scripts/producer.py
```

2. Open Terminal 2:

```bash
python scripts/consumer.py
```

Expected Output:

* Messages from all tenants get processed in a balanced way
* `TenantB` (noisy sender) does not dominate delivery order

---

## 10. Observing Results in AWS Console

### In the SQS Dashboard

1. Navigate to your `FairQueueDemo`
2. Go to the **Monitoring** tab
3. Observe metrics:

   * `NumberOfMessagesSent`
   * `NumberOfMessagesReceived`
   * `ApproximateAgeOfOldestMessage`

These help validate that the queue is processing messages fairly and not getting backlogged.

---

## 11. Cleanup Steps and Security Best Practices

### Delete SQS Queue

To avoid unnecessary charges:

1. Go to the SQS Console
2. Select `FairQueueDemo`
3. Choose "Delete"

### Delete IAM User

If created solely for this demo:

1. Go to the IAM Console
2. Find the user
3. Click "Delete User"

Removing access keys and queues ensures there are no lingering resources that could be misused or cause cost.

---

## 12. Conclusion

This demo project demonstrates how Amazon SQS Fair Queues can be used to create a fair and balanced message delivery system without modifying application-level logic. It is ideal for multi-tenant applications where one tenant may send more messages than others. Using AWS Free Tier, IAM, Boto3, and simple Python scripts, developers can simulate and observe the benefits of this new queue type in real time.
