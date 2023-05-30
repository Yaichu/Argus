# Argus

For Jenkins EC2 run:

aws configure
aws ecr get-login-password --region us-east-1 | sudo docker login --username AWS --password-stdin 161192472568.dkr.ecr.us-east-1.amazonaws.com
docker pull 161192472568.dkr.ecr.us-east-1.amazonaws.com/jenkins-controller
sudo chown -R 1000:1000 /var/jenkins_home
sudo docker run 161192472568.dkr.ecr.us-east-1.amazonaws.com/jenkins-controller

sudo docker run -d -p 8080:8080 -v /var/jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock 161192472568.dkr.ecr.us-east-1.amazonaws.com/jenkins-controller





Needed plugins:
<!-- Git -->
Amazon EC2 plugin
Amazon ECR