
library 'status-jenkins-lib@v1.9.10'

pipeline {
  agent {
    label 'linux'
  }

  options {
    timestamps()
    /* Prevent Jenkins jobs from running forever */
    timeout(time: 10, unit: 'MINUTES')
    /* manage how many builds we keep */
    buildDiscarder(logRotator(
      numToKeepStr: '20',
      daysToKeepStr: '30',
      artifactNumToKeepStr: '1',
    ))
    disableConcurrentBuilds()
    disableRestartFromStage()
  }

  environment {
    GIT_COMMITTER_NAME = 'status-im-auto'
    GIT_COMMITTER_EMAIL = 'auto@status.im'
  }

  stages {
    stage('Deps') {
      steps { script {
        nix.develop('npm install')
      } }
    }

    stage('Build') {
      steps { script {
        nix.develop('npx quartz build')
        jenkins.genBuildMetaJSON('public/build.json')
      } }
    }

    stage('Publish Prod') {
      when { expression { GIT_BRANCH.endsWith('master') } }
      steps { script {
        sshagent(credentials: ['status-im-auto-ssh']) {
          nix.develop('ghp-import -c roadmap.vac.dev -p public', pure: false)
        }
      } }
    }

    stage('Archive') {
      when { expression { !GIT_BRANCH.endsWith('master') } }
      steps {
        archiveArtifacts(artifacts: 'public/**')
      }
    }
  }

  post {
    cleanup { cleanWs() }
  }
}
