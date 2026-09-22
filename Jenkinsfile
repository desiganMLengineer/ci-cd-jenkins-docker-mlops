pipeline {
    agent any
    
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        
        stage('Run Unit Tests') {
            steps {
                echo 'Running automated tests...'
                // If your test file is inside the app folder, update the path accordingly
                sh 'python3 -m unittest discover'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker container image...'
                sh 'docker build -t desigan-mlops-app:latest .'
            }
        }
        
        stage('Deployment Simulation') {
            steps {
                echo 'Deploying application locally using Docker...'
                sh 'docker run --rm desigan-mlops-app:latest'
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline completed successfully! Zero-touch deployment achieved.'
        }
        failure {
            echo 'Pipeline failed. Check test results or code syntax.'
        }
    }
}
