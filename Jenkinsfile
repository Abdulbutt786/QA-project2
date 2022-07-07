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
                sh "ssh abdulbutt@dev-machine '/home/abdulbutt/.local/bin/ansible-playbook -i /home/abdulbutt/gihubrepos/QA-project2/ansible/inventory.yaml /home/abdulbutt/gihubrepos/QA-project2/ansible/playbook1.yaml'"
            }
        }
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
        stage('Deploy'){
            steps{
                sh "scp nginx.conf abdulbutt@docker-manager:home/manager/nginx.conf"
                sh "scp docker-compose.yaml abdulbutt@docker-manager:home/manager/docker-compose.yaml"
                sh "ssh abdulbutt@docker-manger 'docker stack deploy -c docker-compose.yaml Meal'"
            }
        }
    }
}
    