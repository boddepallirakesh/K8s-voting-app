pipeline {
    agent any  // Runs on any available agent
    
    stages {
        stage('Run Python Script') {
            steps {
                script {
                    // Python code to execute Windows CMD commands using subprocess
                    def pythonScript = '''
                        import subprocess
                        result = subprocess.run(["echo", "Hello from Python in Windows CMD!"], capture_output=True, text=True)
                        print(result.stdout)
                    '''
                    
                    // Save the Python script to a file
                    writeFile(file: 'run_python_script.py', text: pythonScript)
                    
                    // Run the Python script using bat (Windows cmd)
                    def result = bat(script: 'python run_python_script.py', returnStdout: true).trim()
                    
                    // Output the result
                    echo "Python Script Output: ${result}"
                }
            }
        }
    }
}
