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
                    python_hw = docker.build("zoglo/python_hw:${env.BUILD_ID}", "-f docker_image/")
                }
            }
        }
    
      stage("Push image") {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
                            myapp.push("latest")
                            myapp.push("${env.BUILD_ID}")
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

  }

}