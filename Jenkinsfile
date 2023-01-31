pipeline {
  agent any
  stages {
    stage('aws-test-s3-access') {
      steps {
        withCredentials([[
        $class: 'AmazonWebServicesCredentialsBinding',
        credentialsId: "iam_user_vijay	",
        accessKeyVariable: 'AWS_ACCESS_KEY_ID',
        secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
    ]])
        { 
        sh 'pip3 install boto3'
        sh "python3 test.py"
          }
    }
  }
}
}