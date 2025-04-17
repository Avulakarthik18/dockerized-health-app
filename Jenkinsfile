pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t health-check-app .'
            }
        }
        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name health-check health-check-app || true'
            }
        }
    }
    post {
        always {
            echo 'Pipeline execution complete.'
        }
    }
}
