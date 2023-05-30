### This project describes a Jenkins pipeline that implements a basic CI strategy in which you
### build an artifact, deploy it, and run a test against it.

The pipeline includes two types of flows, implemented as two separate stages in a single
Jenkinsfile.

* For start, you should configure an AWS EC2 instance with the type of t2.medium at least

For the Jenkins EC2 run the following:

```
aws configure
```
```
aws ecr get-login-password --region [REGION] | sudo docker login --username AWS --password-stdin [ACCOUNT_ID].dkr.ecr.[REGION].amazonaws.com
```
```
docker pull [ACCOUNT_ID].dkr.ecr.[REGION].amazonaws.com/jenkins-controller
```
```
sudo chown -R 1000:1000 /var/jenkins_home
```
```
sudo docker run [ACCOUNT_ID].dkr.ecr.[REGION].amazonaws.com/jenkins-controller
```
```
sudo docker run -d -p 8080:8080 -v /var/jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock [ACCOUNT_ID].dkr.ecr.[REGION].amazonaws.com/jenkins-controller
```


* AWS Credentials are stored in Jenkins Credentials store

* Necessary plugins:

Amazon EC2 
Amazon ECR
Git
Docker
Docker Pipeline
