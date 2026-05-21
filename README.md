# Enterprise Vehicle Insurance Risk Prediction: End-to-End MLOps Pipeline

In the Banking, Financial Services, and Insurance (BFSI) sector, building accurate predictive models for underwriting and claims is only half the battle; deploying them reliably, securely, and at scale is where true business value is realized.

This repository hosts a production-grade, end-to-end Machine Learning Operations (MLOps) pipeline designed for **Vehicle Insurance Prediction**. It features a highly modular Object-Oriented Programming (OOP) architecture, robust logging, exception handling, and an automated CI/CD deployment pipeline tailored for enterprise environments.

## Business Objective

To automate and optimize vehicle insurance risk assessment by predicting policyholder claim probabilities or calculating dynamic premiums based on vehicle and demographic features. This pipeline ensures that the predictive model serving these financial decisions is continuously integrated, evaluated, and deployed without manual intervention.

## Pipeline Architecture

The system is built with a scalable, component-based architecture to handle data drift and strict schema requirements inherent to financial data:

1. **Data Ingestion:** Connects securely to **MongoDB Atlas**, extracting unstructured policy and vehicle telemetry data in key-value format and converting it into structured DataFrames.
2. **Data Validation:** Enforces strict schema validation to ensure data integrity before any financial modeling occurs.
3. **Data Transformation:** Handles feature engineering specific to insurance (e.g., categorical encoding of vehicle models, scaling of driver demographics) and saves artifacts for the inference pipeline.
4. **Model Training:** Trains the predictive risk model using optimized algorithms to minimize false negatives in claim prediction.
5. **Model Evaluation:** Compares the newly trained champion model against the current production model. A strict performance threshold (score improvement of > 0.02) must be met before promoting the new model.
6. **Model Pusher:** Acts as a secure model registry, pushing validated models to an **AWS S3 Bucket** (my-model-mlopsproj773) for version control and retrieval.
7. **Prediction Pipeline:** Exposes a Flask/FastAPI backend serving real-time risk predictions for the underwriting system.

## Tech Stack

| Category | Technologies Used |
| --- | --- |
| **Language** | Python 3.10 |
| **Database** | MongoDB Atlas |
| **Cloud Infrastructure** | AWS (S3, EC2, ECR, IAM) |
| **DevOps & CI/CD** | Docker, GitHub Actions (Self-hosted runner) |
| **Environment Management** | Conda, Virtualenv |

---

## Local Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/vehicle-insurance-mlops.git
cd vehicle-insurance-mlops

```

### 2. Create a Virtual Environment

```bash
conda create -n vehicle python=3.10 -y
conda activate vehicle

```

### 3. Install Dependencies

This project utilizes setup.py and pyproject.toml for local package management.

```bash
pip install -r requirements.txt

```

### 4. Configure Environment Variables

To connect the application to the database and AWS, set the following environment variables. **Never commit these credentials to version control.**

**For Bash / macOS / Linux:**

```bash
export MONGODB_URL="mongodb+srv://<username>:<password>@cluster0.mongodb.net/?appName=Cluster0"
export AWS_ACCESS_KEY_ID="<your_aws_access_key>"
export AWS_SECRET_ACCESS_KEY="<your_aws_secret_key>"

```

**For PowerShell / Windows:**

```powershell
$env:MONGODB_URL="mongodb+srv://<username>:<password>@cluster0.mongodb.net/?appName=Cluster0"
$env:AWS_ACCESS_KEY_ID="<your_aws_access_key>"
$env:AWS_SECRET_ACCESS_KEY="<your_aws_secret_key>"

```

### 5. Run the Application

```bash
python app.py

```

Access the application locally at http://localhost:5000. You can trigger a new model training job by navigating to the /training route.

---

## CI/CD Pipeline & Deployment

Financial models require zero-downtime deployments and strict version control. This project implements a seamless CI/CD pipeline:

* **Containerization:** The application environment is standardized using a Dockerfile, ensuring parity between development and production.
* **GitHub Actions:** Any push to the main branch triggers the aws.yaml workflow for continuous integration.
* **AWS ECR:** The Docker image is built and pushed to the Amazon Elastic Container Registry (vehicleproj).
* **AWS EC2:** A self-hosted GitHub runner deployed on an Ubuntu EC2 instance automatically pulls the latest image and serves the prediction API on port 5080.

### Required GitHub Secrets for CI/CD

To deploy this pipeline in your own environment, configure the following secrets in your repository settings:

* AWS_ACCESS_KEY_ID
* AWS_SECRET_ACCESS_KEY
* AWS_DEFAULT_REGION (e.g., us-east-1)
* ECR_REPO

---

## Project Structure Highlights

* /src/components: Core ML logic (Ingestion, Validation, Transformation, Trainer).
* /src/entity: Defines data contracts and artifact schemas (e.g., DataIngestionConfig, s3_estimator.py).
* /src/configuration: Manages secure external connections (mongo_db_connections.py, aws_connection.py).
* /notebooks: Contains EDA, feature engineering, and data profiling notebooks.
* demo.py: Used for isolated component testing and ensuring the custom BFSI logger and exception handlers function correctly.