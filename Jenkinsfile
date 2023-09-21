pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/Nossston/Autobooking', branch: 'master')
      }
    }

    stage('Log') {
      steps {
        sh '''ls -la
'''
      }
    }

  }
}