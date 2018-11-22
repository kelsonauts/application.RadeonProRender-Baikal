#!Groovy

node('Render') {
	stage('Checkout') {
		deleteDir()
		checkout scm
	}

	stage('Prepare') {
		sh(script: """
			set -x
			pwd
			ls -lah
			git  submodule update --init
			"""
		)
	}

	stage('Build') {
		sh(script: """
			pwd
			mkdir build
			cd build
			cmake -DCMAKE_BUILD_TYPE=Debug ..
			make -j4
			cd ..
			pwd
			"""
		)
	}

	stage('Test') {
		sh(script: """
			pwd
			cd BaikalTest
			../build/bin/BaikalTest -genref 1
			"""
		)
	}

	stage('Clean workspace') {
		cleanWs()	
	}
}