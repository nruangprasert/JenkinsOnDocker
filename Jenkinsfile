pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/nruangprasert/JenkinsOnDocker.git', branch: 'main'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-monitoring-app .'
            }
        }
        stage('Stop Existing Flask Container') {
    steps {
        script {
            sh 'docker ps -q --filter "ancestor=flask-monitoring-app" | xargs -r docker stop'
            sh 'docker ps -a -q --filter "ancestor=flask-monitoring-app" | xargs -r docker rm'
        }
    }
}

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name flask-container flask-monitoring-app'
            }
        }
        stage('Test') {
            steps {
                sh 'docker run flask-monitoring-app pytest test_app.py'
            }
        }
    }
}