pipeline {
  agent any
  stages {
    stage('Pull') {
      steps {
        git(url: 'https://github.com/nadavbuc/jenkins_base', branch: 'master')
      }
    }
    stage('run') {
      steps {
        retry(count: 3) {
          sh '''#!/bin/bash
python py/main.py $retrynum blabla'''
        }
        
      }
    }
  }
  environment {
    retrynum = '$retry'
  }
}