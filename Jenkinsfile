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

	stage('Package') {
		sh(script: """
			cd build
			make package
			cd ..
			"""
		)
	}

	stage('Test') {
		sh(script: """
			cd BaikalTest
			../build/bin/BaikalTest -genref 1
			cd ..
			"""
		)
	}

	stage('Push to s3') {
		sh(script: """
			python Tools/scripts/generate_html.py BaikalTest/ReferenceImages index.html
			aws s3 sync BaikalTest/ReferenceImages s3://infrastructure-storages-useast1-static-website/BaikalTest/ReferenceImages/
			aws s3 cp index.html s3://infrastructure-storages-useast1-static-website/
			"""
		)
	}

	stage('Clean workspace') {
		cleanWs()	
	}
}