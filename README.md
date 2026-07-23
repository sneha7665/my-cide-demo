# 🚀 AWS CI/CD Pipeline with Automated Deployment

> An end-to-end CI/CD pipeline integrating **GitHub**, **AWS CodePipeline**, **AWS CodeBuild**, and **AWS Elastic Beanstalk** to automate application deployment with build validation, monitoring, and real-time email alerts using **Amazon CloudWatch** and **Amazon SNS**.

---

## 📌 Overview

This project demonstrates a production-style Continuous Integration and Continuous Deployment (CI/CD) pipeline on AWS.

Whenever code is pushed to the **main** branch, the pipeline automatically:

- Detects source code changes
- Builds and validates the application
- Deploys the application to AWS Elastic Beanstalk
- Monitors deployment failures
- Sends real-time email notifications if the pipeline fails

The project eliminates manual deployment steps while improving deployment speed, reliability, and monitoring.

---

# 📸 Project Screenshots

> Replace the images below with screenshots from your project.

## 1️⃣ AWS CodePipeline

- Successful Source
- Build
- Deploy stages



<img width="1600" height="661" alt="codepipeline-success" src="https://github.com/user-attachments/assets/bb9ea842-5ced-4913-a8cd-d188833287c0" />


---

## 2️⃣ Elastic Beanstalk Application

Running Flask application



<img width="1600" height="848" alt="elastic-beanstalk-app" src="https://github.com/user-attachments/assets/7a1391e2-011c-49f2-9b98-6fd9cb1dbff7" />


## 3️⃣ CloudWatch Alarm

ExecutionFailed metric monitoring


<img width="1600" height="665" alt="cloudwatch-alarm" src="https://github.com/user-attachments/assets/7f8e7907-a5ee-4d9f-8935-aba75bfffed3" />



---

## 4️⃣ SNS Email Notification

Failure alert delivered via email


<img width="1600" height="713" alt="sns-email-alert" src="https://github.com/user-attachments/assets/5f0da80b-95e4-4933-999a-6676eb91517f" />



---

# 🏗 Architecture

```text
                    GitHub Repository
                           │
                           ▼
                  AWS CodePipeline
                           │
          ┌────────────────┴────────────────┐
          ▼                                 ▼
   AWS CodeBuild                 Elastic Beanstalk
(Build & Validation)         (Deployment Platform)
                                          │
                                          ▼
                                     EC2 Instance
                                          │
                                          ▼
                                  Flask Application

                  ▲
                  │
          Amazon CloudWatch
                  │
                  ▼
             Amazon SNS
                  │
                  ▼
          Email Notifications
```

---

# ⚙ Pipeline Workflow

| Stage | AWS Service | Purpose |
|--------|-------------|----------|
| Source | GitHub + CodeConnections | Detects code changes automatically |
| Build | AWS CodeBuild | Installs dependencies and validates code |
| Deploy | Elastic Beanstalk | Deploys Flask application |
| Monitor | CloudWatch | Monitors pipeline failures |
| Alert | Amazon SNS | Sends email notifications |

---

# 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python |
| Framework | Flask |
| Version Control | Git & GitHub |
| CI/CD | AWS CodePipeline |
| Build Service | AWS CodeBuild |
| Deployment | AWS Elastic Beanstalk |
| Compute | Amazon EC2 |
| Web Server | Gunicorn |
| Reverse Proxy | Nginx |
| Monitoring | Amazon CloudWatch |
| Notifications | Amazon SNS |
| Identity & Access | AWS IAM |

---

# 📂 Project Structure

```text
aws-cicd-pipeline/
│
├── application.py
├── requirements.txt
├── buildspec.yml
├── Procfile
├── README.md
└── images/
    ├── codepipeline-success.png
    ├── elastic-beanstalk-app.png
    ├── cloudwatch-alarm.png
    └── sns-email-alert.png
```

---

# ✨ Features

## ✅ Automated CI/CD

- Automatically triggers on every push to the **main** branch.
- No manual deployment required.

---

## ✅ Build Validation

Before deployment, CodeBuild automatically:

- Installs dependencies
- Validates Python syntax
- Imports the application
- Stops deployment if validation fails

Example:

```bash
python -m py_compile application.py

python -c "from application import application"
```

---

## ✅ Automated Deployment

Elastic Beanstalk automatically:

- Creates EC2 instances
- Configures Gunicorn
- Configures Nginx
- Deploys the Flask application

No manual server configuration is required.

---

## ✅ Monitoring

Amazon CloudWatch continuously monitors:

- Pipeline execution
- Deployment status
- Failure metrics

---

## ✅ Real-Time Alerts

If deployment fails:

CloudWatch →

SNS →

Email Notification

Users receive deployment failure notifications within minutes.

---

# 🚀 Deployment Guide

## Step 1 — Create Elastic Beanstalk

- Create a Python environment
- Platform: Python 3.x
- Environment Type: Single Instance
- Instance Type: t2.micro (Free Tier)

---

## Step 2 — Create CodeBuild Project

Configure:

- Source: GitHub
- Buildspec: `buildspec.yml`

---

## Step 3 — Create CodePipeline

Stages:

```
GitHub
    ↓
CodeBuild
    ↓
Elastic Beanstalk
```

---

## Step 4 — Configure Monitoring

Create:

- CloudWatch Alarm
- SNS Topic
- Email Subscription

---

# 🧪 Testing

## Successful Deployment

```bash
git add .
git commit -m "Updated application"
git push origin main
```

Pipeline automatically:

- Detects commit
- Builds application
- Deploys application

---

## Failure Scenario

Break the application intentionally:

```python
from flask import
```

Push:

```bash
git push origin main
```

Result:

- Build fails
- CloudWatch Alarm triggers
- SNS Email Notification is sent

---

# 📈 Results

| Metric | Manual Process | Automated Pipeline |
|---------|----------------|--------------------|
| Deployment Time | ~30 Minutes | ~5 Minutes |
| Build Validation | Manual | Automatic |
| Deployment | Manual | Automatic |
| Failure Detection | Manual | < 2 Minutes |
| Notifications | None | Email Alerts |

---

# 📚 Key Learnings

- AWS CodePipeline
- AWS CodeBuild
- AWS Elastic Beanstalk
- Amazon EC2
- Amazon CloudWatch
- Amazon SNS
- AWS IAM Roles & Policies
- GitHub Integration
- CI/CD Best Practices
- Automated Deployment Strategies
- Deployment Troubleshooting

---

# 💰 Cleanup

To avoid unnecessary AWS charges:

Delete:

- Elastic Beanstalk Environment
- CodePipeline
- CodeBuild Project
- CloudWatch Alarm
- SNS Topic

---

# 👩‍💻 Author

**Sneha Airodagi**

- GitHub: https://github.com/sneha7665

---

# ⭐ If you found this project useful

Please consider giving the repository a ⭐ on GitHub.

It motivates me to build more cloud and DevOps projects.
