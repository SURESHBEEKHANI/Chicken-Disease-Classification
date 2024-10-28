# Chicken Disease Classification Project - AWS Deployment

This project classifies chicken diseases using a machine learning model and deploys it on AWS with a CI/CD pipeline powered by GitHub Actions.

---

## Project Structure

1. **Configuration Files**:
   - `config.yaml`: Contains base settings and parameters for the model and pipeline.
   - `secrets.yaml` [Optional]: Stores sensitive information.
   - `params.yaml`: Adjustable parameters for training and evaluation.

2. **Core Code Files**:
   - `src/config`: Manages configuration across the project.
   - `src/components`: Scripts for data processing, model training, and evaluation.
   - `src/pipeline`: Orchestrates the model pipeline.
   - `main.py`: Main entry point for executing the project.
   - `dvc.yaml`: DVC configuration for versioning the pipeline stages.

---

## Setup Instructions

### Step-by-Step Setup

1. **Clone the Repository**:

   ```sh
   git clone https://github.com/SURESHBEEKHANI/Chicken-Disease-Classification.git
Set Up the Conda Environment:

After navigating to the project directory, create and activate a Conda environment:

conda create -n cnncls python=3.8 -y
conda activate cnncls
Install Requirements:


pip install -r requirements.txt
Run the Application:

python app.py
Access the Application:

Open your browser and navigate to the local host and port specified in the project to access the application.
Data Version Control with DVC
To manage data and model stages with DVC, use the following commands:

dvc init
dvc repro
dvc dag
AWS CI/CD Deployment with GitHub Actions
AWS Setup
AWS Console: Log in and configure necessary AWS resources.

Create an IAM User with permissions for:
EC2 Access: For virtual machine management.
ECR Access: To store Docker images.
Docker Image and EC2 Deployment:

Build Docker Image: Create a Docker image from the project source code.
Push to ECR: Upload the Docker image to the AWS Elastic Container Registry (ECR).
Launch EC2 Instance: Start an EC2 instance to run the Docker image.
Pull and Run Docker Image on EC2: Use EC2 to pull and run the Docker image from ECR.
Required IAM Policies
Attach the following policies to the IAM user for permissions:

AmazonEC2ContainerRegistryFullAccess
AmazonEC2FullAccess
Steps for AWS Deployment
Create an ECR Repository:

Create a repository in ECR and save the URI, for example:
plaintext
Copy code
566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken
Set Up EC2 and Install Docker:

After SSH-ing into the EC2 instance, run the following commands to install Docker:



sudo apt-get update -y
sudo apt-get upgrade -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
Configure EC2 as a Self-Hosted Runner in GitHub:

Go to Settings > Actions > Runners in your GitHub repository.
Set up a new self-hosted runner by selecting the OS and following the displayed commands.
Add GitHub Secrets for Deployment:

In your GitHub repository’s settings, add the following secrets:

AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION: us-east-1
AWS_ECR_LOGIN_URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com
ECR_REPOSITORY_NAME: chicken
This README provides detailed instructions for setting up, running, and deploying the Chicken Disease Classification project on AWS with CI/CD enabled through GitHub Actions.