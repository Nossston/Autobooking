pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/Nossston/Autobooking', branch: 'master')
      }
    }

    stage('Log') {
      parallel {
        stage('Log') {
          steps {
            sh '''ls -la
'''
          }
        }

        stage('Unit test') {
          steps {
            sh 'python3 run.py'
          }
        }

      }
    }

  }
}