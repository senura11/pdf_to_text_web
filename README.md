// Installation Guide for PythonAnywhere (TypeScript Example)

/**
 * Steps to deploy the PDF to Text Web project on PythonAnywhere.
 */

interface DeploymentSteps {
  step1: string;
  step2: string;
  step3: string;
  step4: string;
  step5: string;
  step6: string;
}

const deploymentSteps: DeploymentSteps = {
  step1: "Create a PythonAnywhere account and log in.",
  step2: "Clone the GitHub repository using 'git clone https://github.com/senura11/pdf_to_text_web.git'.",
  step3: "Set up a virtual environment and install dependencies using 'pip install -r requirements.txt'.",
  step4: "Configure the Flask application in the PythonAnywhere dashboard.",
  step5: "Set up static files and templates in the PythonAnywhere dashboard.",
  step6: "Reload the web app and access it via the provided URL.",
};

console.log("Deployment Steps:");
console.log(deploymentSteps);
