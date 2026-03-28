pipeline {
    agent any
    
    // Pulling the secure keys from Jenkins Credentials using their IDs
    environment {
        // Use the ID name you gave it in Jenkins, e.g., 'gemini-api-key'
        GEMINI_API_KEY = credentials('gemini-api-key')
        
        // Use the ID name you gave it in Jenkins, e.g., 'github-token'
        GITHUB_CREDS = credentials('github-token')
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'pip install google-genai'
            }
        }
        
        stage('Generate Documentation') {
            steps {
                // Run the Python script we created in Phase 1
                sh 'python generate_docs.py'
            }
        }
        
        stage('Commit and Push README') {
            steps {
                script {
                    sh '''
                        git config user.name "Aayush-Birari"
                        git config user.email "aayush.birari12@gmail.com"
                        
                        # Add the newly generated README
                        git add README.md
                        
                        # Commit the changes. The [skip ci] tag is CRITICAL. 
                        # It stops Jenkins from triggering another build when it pushes this commit.
                        git diff-index --quiet HEAD || git commit -m "docs: Auto-update README by AI [skip ci]"
                        
                        # Push back to GitHub using the credentials
                        git push https://${GITHUB_CREDS_USR}:${GITHUB_CREDS_PSW}@github.com/Aayush-Birari/Auto_Documentor.git HEAD:main
                    '''
                }
            }
        }
    }
}
