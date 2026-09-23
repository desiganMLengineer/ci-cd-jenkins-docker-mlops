# End-to-End MLOps CI/CD Pipeline

Welcome to my portfolio It's My First Devops Project! This repository demonstrates a fully automated **Continuous Integration and Continuous Deployment (CI/CD)** pipeline built from scratch for a machine learning inference application. 

If you've ever wondered how modern tech companies automatically test machine learning code, build secure software containers, and deploy ML models live the exact second a developer pushes a git commit—this project builds that exact workflow locally using **Jenkins, Docker, Python, Scikit-Learn, GitHub Webhooks, Ngrok, and Linux**.


##  What Problem Does This Solve?

In traditional software development and machine learning, data scientists train models on their laptops, but moving those models into production is often manual, messy, and prone to breaking. This leads to the infamous phrase: *"It worked on my machine!"*

**MLOps (Machine Learning Operations)** solves this by automating the entire lifecycle. With this pipeline:
1. Every time code changes, automation servers take over instantly.
2. Code and model logic are tested in a clean, isolated environment using `pytest`.
3. The machine learning application (featuring a **Scikit-Learn Random Forest Classifier**) is packaged into a **Docker container** to ensure it runs identically anywhere.
4. The latest version of the ML inference service is automatically deployed live without human intervention.


## 🛠️ The Tech Stack & Architecture

Here is the exact technology stack used to power this project:

* **Version Control:** Git & GitHub (hosting the source code and triggering events).
* **Automation Server:** Jenkins (running locally on an Ubuntu virtual machine to orchestrate the pipeline).
* **Event Bridge:** Ngrok / GitHub Webhooks (securely bridging GitHub push events to the local Jenkins server in real-time).
* **Containerization:** Docker (packaging the Python app, ML model, dependencies, and runtime into a lightweight container).
* **Machine Learning & Testing:** Python, **Scikit-Learn** (Random Forest model trained on the Iris dataset), Flask (API inference endpoint), and Pytest.
* **Operating System:** Linux (Ubuntu via VirtualBox CLI).


##  End-to-End Architecture Flow

```text
[ Developer / Git Push ] 
        │
        ▼ (Triggers via GitHub Webhook & Ngrok)
[ Jenkins Automation Server ]
        ├── Stage 1: Checkout Code (Clones latest repository state)
        ├── Stage 2: Run Unit Tests (Spins up a virtual environment & runs Pytest)
        ├── Stage 3: Build Docker Image (Packages app, Scikit-Learn, & requirements into an image)
        └── Stage 4: Deploy Container (Stops old container & launches fresh ML inference instance on Port 5001)
📂 Project Directory Structure
Plaintext
ci-cd-jenkins-docker-mlops/
│
├── app/
│   ├── main.py          # Flask ML inference web app (Random Forest / Iris Classifier)
│   └── test_main.py     # Pytest unit test suite verifying app health and model responses
│
├── Dockerfile           # Multi-layer container instructions for Python runtime
├── Jenkinsfile          # Declarative multi-stage CI/CD pipeline script
├── requirements.txt     # Python package dependencies (Flask, Pytest, Scikit-Learn)
└── README.md            # Project documentation

⚙️ Step-by-Step Pipeline Breakdown (A to Z)

Every stage in the Jenkinsfile serves a specific purpose in ensuring production-grade reliability:

1. Checkout Code
What happens: Jenkins connects to this GitHub repository, pulls down the latest commit, and stages the files into its local workspace.

Real-world analogy: Like a quality inspector grabbing the newest blueprints off the desk before starting assembly.

2. Run Unit Tests
What happens: Jenkins creates an isolated Python virtual environment (test_env), installs all dependencies from requirements.txt (including Scikit-Learn and Flask), and executes pytest.

Real-world analogy: Running crash tests on a car engine in a controlled laboratory before putting it into a vehicle. If a single test fails, the pipeline halts immediately to prevent broken code from deploying.

3. Build Docker Image
What happens: Using the Dockerfile, Docker bundles Python 3.10-slim, the source code, Scikit-Learn, and all required libraries into a standardized image tagged as desigapperumal-mlops-app:latest.

Real-world analogy: Packing goods into a standardized shipping container so it fits on any ship, train, or truck anywhere in the world without damage.

4. Deploy Container
What happens: The pipeline executes shell commands to safely stop and remove any older running container (mlops-container), then launches a brand new container instance running model inference, mapping host port 5001 to container port 5000.

Real-world analogy: Swapping out an old machinery part in a factory line with a brand new, pre-tested upgrade with zero downtime.

# How to Verify and Run Locally

If you want to spin up or test this project on your own local Ubuntu environment:

Clone the Repository:

Bash
git clone [https://github.com/desiganMLengineer/ci-cd-jenkins-docker-mlops.git](https://github.com/desiganMLengineer/ci-cd-jenkins-docker-mlops.git)
cd ci-cd-jenkins-docker-mlops
Run Unit Tests Manually:

Bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest app/test_main.py
Build and Run Docker Container Locally:

Bash
docker build -t desigapperumal-mlops-app:latest .
docker run -d -p 5001:5000 --name mlops-container desigapperumal-mlops-app:latest
Test the Live ML Inference Endpoint:

Bash
curl http://localhost:5001/
👤 Author
Desigapperumal N — B.Tech IT 2026 Graduate & Devops Engineering / MLOps Engineer

 GitHub Profile - github.com/desiganMLengineer
