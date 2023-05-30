pipeline {
    agent any
    environment {
        BRANCH_NAME = 'main'
    }
    stages {
        stage('Build & Deploy') {
            when {
                branch 'main' 
            }
        
            steps {
                script {
                    def branchName = "${BRANCH_NAME}"

                    // Clone the GIT repository and checkout the branch
                    git branch: branchName, url: 'https://github.com/Yaichu/Argus.git'

                    // Print the current branch for verification
                    sh 'git branch --show-current'
                }

                // Build the Docker image
                sh 'sudo chmod 777 /var/run/docker.sock'
                sh 'docker build -t datetimeos .'
                sh 'echo "Finished to build datetimeos image"'

                // Run the Python script inside the container
                sh 'echo "Starting to run the image..."'
                sh 'docker run datetimeos'
                sh 'docker ps -a'

                // Deploy the artifact to S3
                sh 'echo "Deploying the artifact to S3"'

                // Authenticate with AWS
                withCredentials([[
                    $class: 'AmazonWebServicesCredentialsBinding',
                    credentialsId: 'aws-creds'
                    ]])
                 {
                    sh 'aws s3 cp ./output.txt s3://yael-frenkel'
                 }
                sh 'echo "Deploying the Docker image to ECR"'
                script {
                    docker.withRegistry('https://161192472568.dkr.ecr.us-east-1.amazonaws.com', 'ecr:us-east-1:aws-creds') {
                        def Image = docker.build("yael-frenkel")
                        Image.push("latest")
                    }
                }
            
            }
        }
        
        stage('Pull & Test') {
            // Trigger the stage every day at 8
            // triggers {
            //     cron('0 8 * * *')
            // }

            steps {
                // Trigger the stage manually from the Jenkins UI
                input (message: 'Do you want to run the Pull & Test stage?', ok: 'Yes')
                withCredentials([[
                    $class: 'AmazonWebServicesCredentialsBinding',
                    credentialsId: 'aws-creds'
                ]]) {
                    script {
                        // Download the most recent artifact from S3
                        def artifactPath = sh(script: 'aws s3 cp s3://yael-frenkel/output.txt . --recursive --include "*.txt" --no-progress', returnStdout: true).trim()
    
                        // Check if the artifact is empty
                        def isArtifactEmpty = sh(script: '[[ ! -s output.txt ]] && echo "Artifact is empty" || echo "Artifact is not empty"', returnStatus: true)
    
                        // Print the test results to the console output
                        echo isArtifactEmpty == 0 ? "Test Result: Artifact is empty" : "Test Result: Artifact is not empty"
                    }
                }
            }
        }    
    }
}    
