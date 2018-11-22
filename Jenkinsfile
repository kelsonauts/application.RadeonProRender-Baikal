#!Groovy

node('Render') {
	stage('Checkout') {
		deleteDir()
		checkout scm
	}

	stage('Prepare') {
		sh(script: """
			set -x
			ls -lah
			git  submodule update --init
			"""
		)
	}

	stage('Build') {
		sh(script: """
			mkdir build
			cd build
			cmake -DCMAKE_BUILD_TYPE=Debug ..
			make -j4
			cd ..
			"""
		)
	}

	stage('Test') {
		sh(script: """
			cd BaikalTest
			../build/bin/BaikalTest -genref 1
			"""
		)
	}

	stage('Clean workspace') {
		cleanWs()	
	}
}