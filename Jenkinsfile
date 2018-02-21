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
        sh '''#!/bin/bash
python py/main.py 3 blabla'''
      }
    }
    stage('finish') {
      steps {
        echo 'tobe continued'
      }
    }
  }
}