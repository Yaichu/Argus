pipeline {
    agent any
    
    environment {
        BRANCH_NAME = 'main'
    }
    stages {
        stage('Build & Deploy') {
            // when {
            //     // Trigger the stage if a new push has been made to the pull request branch or chosen manually by a user from the Jenkins UI
            //     
            // }
            steps {
                script {
                    def branchName = "${BRANCH_NAME}"
                    
                    // Clone the GIT repository and checkout the branch
                    git branch: branchName, url: 'https://github.com/Yaichu/Argus.git'
                    
                    sh 'git branch --show-current'
                }
                
                // Build the Docker image
                sh 'sudo chmod 777 /var/run/docker.sock'
                sh 'docker build -t datetimeos .'
                
                // Run the Python script inside the container
                sh 'docker run datetimeos'
                
                // Deploy the artifact to S3
                withAWS(region: 'us-east-1', credentials: 'aws-creds') {
                    sh 'aws s3 cp ./output.txt s3://yael-frenkel'
                }
  
                // Deploy the Docker image to ECR
                withCredentials([
                credentials(credentialsId: 'aws-creds') //, usernameVariable: 'AWS_ACCESS_KEY_ID', passwordVariable: 'AWS_SECRET_ACCESS_KEY')
                ]) {
                sh '''
                    $(aws ecr get-login --no-include-email --region us-east-1)
                    docker tag datetimeos:latest yael-frenkel/datetimeos:latest
                    docker push yael-frenkel/datetimeos:latest
                '''
                }
            
            

            }
        }

        stage('Pull & Test') {

        }

    }
}
