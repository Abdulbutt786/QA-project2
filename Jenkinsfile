pipeline{
    agent any
    stages{
        stage('App Testing'){
            steps{
                sh "bash test.sh"
            }
        }
        stage('Ansible playbook run'){
            steps{
                sh '''ssh abdulbutt@dev-machine \'/home/abdulbutt/.local/bin/ansible-playbook -i gihubrepos/QA-project2/ansible/inventory.yaml 
                gihubrepos/QA-project2/ansible/playbook1.yaml\''''
            }} 
        stage('Building and pushing images'){
            environment{
                DOCKERHUB_USERNAME=credentials('DOCKER_UNAME')
                DOCKERHUB_PASSWORD=credentials('DOCKER_PWORD')
            }
            steps{
                sh "docker-compose build --parallel"
                sh "docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PASSWORD"
                sh "docker-compose push"
            }
        }
        }
    }