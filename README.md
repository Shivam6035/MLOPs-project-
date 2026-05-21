# MLOPs-project-
Here is a professional, recruiter-ready README.md template based on your workflow.

I have structured it to highlight your MLOps, Data Engineering, and CI/CD skills. **Crucially, I have removed the hardcoded MongoDB passwords and AWS keys that were in your raw notes.** Never expose credentials in a public GitHub repository, as it is a major red flag for recruiters.

Copy and paste the markdown below into your repository's README.md file.

---

# End-to-End Vehicle Data MLOps Pipeline

This repository hosts a complete, production-ready Machine Learning Operations (MLOps) pipeline for vehicle data processing and prediction. It features a fully modular Object-Oriented Programming (OOP) architecture, custom logging and exception handling, and an automated CI/CD deployment pipeline using Docker, GitHub Actions, and AWS.

## Pipeline Architecture

The project is built with a highly scalable, component-based architecture:

1. **Data Ingestion:** Connects to **MongoDB Atlas**, fetches unstructured data in key-value format, and transforms it into structured DataFrames.
2. **Data Validation:** Validates data schema and integrity against predefined configurations.
3. **Data Transformation:** Cleans, scales, and prepares features for model consumption, storing artifacts for inference.
4. **Model Training:** Trains the predictive model using optimized machine learning algorithms.
5. **Model Evaluation:** Compares the newly trained model against the current production model (threshold score: 0.02).
6. **Model Pusher:** Acts as a model registry, pushing validated models to an **AWS S3 Bucket** (my-model-mlopsproj773).
7. **Prediction Pipeline:** Serves predictions via a web application interface using a Flask/FastAPI backend.

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
git clone https://github.com/your-username/vehicle-mlops-pipeline.git
cd vehicle-mlops-pipeline

```

### 2. Create a Virtual Environment

```bash
conda create -n vehicle python=3.10 -y
conda activate vehicle

```

### 3. Install Dependencies

This project uses setup.py and pyproject.toml for local package management.

```bash
pip install -r requirements.txt

```

### 4. Configure Environment Variables

To connect the application to your database and cloud storage, set the following environment variables in your terminal (or .env file):

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

Access the application locally at http://localhost:5000. You can trigger model training by navigating to the /training route.

---

## CI/CD Pipeline & Deployment

This project implements a seamless continuous integration and continuous deployment pipeline:

* **Containerization:** The application environment is standardized using a Dockerfile.
* **GitHub Actions:** Any push to the main branch triggers the aws.yaml workflow.
* **AWS ECR:** The Docker image is built and pushed to the Amazon Elastic Container Registry.
* **AWS EC2:** A self-hosted GitHub runner deployed on an Ubuntu EC2 instance automatically pulls the latest image and serves it on port 5080.

### Required GitHub Secrets for CI/CD

To fork and deploy this project yourself, configure the following secrets in your repository settings (Settings > Secrets and variables > Actions):

* AWS_ACCESS_KEY_ID
* AWS_SECRET_ACCESS_KEY
* AWS_DEFAULT_REGION (e.g., us-east-1)
* ECR_REPO

---

## Project Structure Highlights

* /src/components: Contains modular scripts for data ingestion, validation, transformation, and model training.
* /src/entity: Defines the configurations and artifact schemas (e.g., DataIngestionConfig, s3_estimator.py).
* /src/configuration: Manages external connections (mongo_db_connections.py, aws_connection.py).
* /notebooks: Contains EDA and Feature Engineering Jupyter notebooks.
* demo.py: Used for isolated testing of custom loggers, custom exception handlers, and individual components.