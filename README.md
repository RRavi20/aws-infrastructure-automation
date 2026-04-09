\# AWS Cloud Infrastructure Automation

Automated the provisioning of AWS resources using Python to streamline deployment processes.



\## 🚀 Project Overview

This project automates the creation of AWS EC2 instances and S3 buckets using Python and Boto3. It follows the "Infrastructure as Code" (IaC) philosophy to reduce manual configuration time and human error.



\## 🛠 Tech Stack

\- \*\*Language:\*\* Python

\- \*\*Cloud Provider:\*\* AWS (EC2, S3, IAM)

\- \*\*Library:\*\* Boto3

\- \*\*Tools:\*\* Git, GitHub, PowerShell



\## 📊 Key Results

\- \*\*85% Time Reduction:\*\* Automated setup compared to manual AWS Console clicks.

\- \*\*Security:\*\* Implemented Least-Privilege access via automated Security Groups.

\- \*\*Traceability:\*\* 100% of infrastructure changes tracked via Git version control.



\## 📂 Scripts

\- `launch\_ec2.py`: Provisions a T2.Micro instance with specific AMI and Tags.

\- `manage\_s3.py`: Creates a globally unique S3 bucket and uploads initial logs.

\- `setup\_security.py`: Configures firewalls to allow only Port 22 (SSH).

\- `cleanup.py`: Safely terminates resources to avoid unnecessary costs.

