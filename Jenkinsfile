pipeline {
  agent any
  stages {
    stage('aws-test-s3-access') {
      steps {
        
        '''
        sh 'pip3 install boto3'
        sh "python3 test.py"
        '''
    
  }
}
}