#!Groovy

node('Render') {
	stage('Checkout') {
		checkout scm
		deleteDir()
	}

	stage('Prepare') {
		sh(script: """
			set -x
			git  submodule update --init
			"""
		)
	}

	stage('Build') {
		sh(script: """
			mkdir build
			cd build
			cmake -DCMAKE_BUILD_TYPE=Debug ..
			make
			"""
		)
	}

	stage('Test') {
		sh(script: """
			cd ../BaikalTest
			../RprTest/BaikalTest -genref 1
			"""
		)
	}
}