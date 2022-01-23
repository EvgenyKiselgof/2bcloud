pipeline {

  agent any

  stages {

    stage('Checkout Source') {
      steps {
        git url:'https://github.com/EvgenyKiselgof/2bcloud.git', branch:'main'
      }
    }
    
      stage("Build image") {
            steps {
                script {
                    python_hw = docker.build("zoglo/python_hw:${env.BUILD_ID}")
                }
            }
        }
    
      stage("Push image") {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
                            python_hw.push("latest")
                            python_hw.push("${env.BUILD_ID}")
                    }
                }
            }
        }

    
    stage('Deploy App') {
      steps {
        script {
          kubernetesDeploy(configs: "k8s_app/hello_world.yml", kubeconfigId: "kubeconfig")
        }
      }
    }
    
    
    stage('Start Tunnel and Ngrok') {
      steps {
        sh '''
        minikube tunnel > /dev/null &
        /home/evgeny/ngrok http 10.102.167.217:8081 --log=stdout > ngrok.log &
        '''
      }
    }

    stage('Validate response from App by ClusterIP') {
      steps {
        sh ''' curl 10.102.167.217:8081 '''
            }
    }
        stage('Get External URL') {
      steps {
        sh ''' sed -ne 's/.*\\(http:[^"]*\\).*/\\1/p' < /home/evgeny/ngrok.log | awk 'NR == 1' '''
            }
    }
  }

}
