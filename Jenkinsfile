pipeline {
    agent any

	 stage("Aws test credentials"){
            steps{
                withAWS(credentials: 'AKIAWMQAZAWU5GGSRL53', region: 'ap-south-1'){
            
                    s3Upload (acl: 'Private' , bucket: 'vaishdevops5112025' , file: 'my.zip')
                   

                }
            }
        }

    stages {

        stage('Test') {
            steps {
                sh 'python3 -m unittest discover tests'
            }
        }
    }

    post {
        success {
            echo 'All tests passed and package built successfully!Meow!'
        }
        failure {
            echo 'Something went wrong during the pipeline! :('
        }
    }
}
