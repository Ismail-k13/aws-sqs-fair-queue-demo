project: **AWS SQS Fair Queue Demo**. This version provides complete setup instructions for developers using AWS Free Tier.

---
# AWS SQS Fair Queue Demo

A hands-on demo showing how to use the new **Amazon SQS Fair Queues** feature to handle multi-tenant message fairness without code-level throttling or priority logic.

>  Built with Python, Boto3, and AWS Free Tier  
>  Simulates noisy vs. quiet tenants and shows how SQS fairly processes their messages.

---

## What Are SQS Fair Queues?

**Fair Queues** are a new SQS queue type introduced in 2025 to **detect and slow down noisy tenants**, giving fair processing time to quieter senders.

> [🔗 Official AWS Blog Post](https://aws.amazon.com/blogs/aws/amazon-sqs-fair-queues-now-available/)

---

## 📁 Project Structure

```text
aws-sqs-fair-queue-demo/
│
├── scripts/
│   ├── producer.py      # Sends messages from multiple tenants
│   └── consumer.py      # Receives and prints messages
│
├── assets/
│   └── screenshots/     # Screenshots of queue setup, monitoring, etc.
│
├── .gitignore
├── README.md
└── requirements.txt
````

---

## 🛠️ Prerequisites

* ✅ AWS Free Tier account
* ✅ IAM user with SQS permissions
* ✅ Python 3.8+
* ✅ AWS CLI configured
* ✅ Boto3 installed

```bash
pip install boto3
```

---

##  Setup Guide

### 1. Create a Fair Queue on AWS

* Go to [Amazon SQS Console](https://console.aws.amazon.com/sqs/)
* Click **Create Queue**
* Choose **Fair Queue**
* Name it: `FairQueueDemo`
* Keep defaults and click **Create Queue**

### 2. Configure IAM User

Ensure your IAM user has this policy attached:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "sqs:SendMessage",
        "sqs:ReceiveMessage",
        "sqs:DeleteMessage",
        "sqs:GetQueueUrl",
        "sqs:GetQueueAttributes"
      ],
      "Resource": "*"
    }
  ]
}
```

### 3. Clone the Repo and Run Scripts

```bash
git clone https://github.com/Your_Github_Name/aws-sqs-fair-queue-demo.git
cd aws-sqs-fair-queue-demo
pip install -r requirements.txt
```

---

##  How It Works

### `producer.py`

* Sends messages from 3 tenants: `TenantA`, `TenantB`, and `TenantC`
* Simulates noisy behavior from `TenantB`
* SQS Fair Queue ensures fairness without throttling logic

```bash
python scripts/producer.py
```

###  `consumer.py`

* Continuously polls and processes messages
* Fair Queue prioritizes messages from quieter tenants

```bash
python scripts/consumer.py
```

---

##  View Monitoring

In the AWS SQS Console:

* Go to your **FairQueueDemo**
* Click on the **Monitoring** tab
* View metrics like:

  * `NumberOfMessagesSent`
  * `NumberOfMessagesReceived`
  * `ApproximateAgeOfOldestMessage`

---

##  Why Use Fair Queues?

* 📦 No need for tenant-level rate limiting in app code
* ⚖️ Automatic fairness and priority
* 🚫 Prevent noisy tenants from starving others
* 🔒 Works within AWS Free Tier

---

## 🧪 Tested With

* ✅ Region: `Your Region` ( AWS Free Tier eligible)
* ✅ SQS Fair Queue
* ✅ Python 3.11
* ✅ Boto3 1.34+

---

## 🙌 Acknowledgements

* [AWS Official Blog on Fair Queues](https://aws.amazon.com/blogs/aws/amazon-sqs-fair-queues-now-available/)
* AWS Boto3 SDK
* AWS Free Tier

---

## 📸 Screenshots

*Screenshots for queue creation, CloudWatch metrics, and sample outputs go here*

> Add them under `/assets/screenshots/` and link them here.

---

## ⭐️ Star the Repo

If this helped you understand SQS Fair Queues, please ⭐️ the repo:
👉 [https://github.com/Ismail-k13/aws-sqs-fair-queue-demo](https://github.com/Ismail-k13/aws-sqs-fair-queue-demo)

```