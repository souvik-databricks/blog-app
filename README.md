# Support Repository for the `Databricks Apps - Hands-on` blog series

Databricks Apps, a fastest way to build data and AI applications and deploy within Databricks. Following the announcement of the public preview of Databricks Apps, here in this series of blogs we will showcase patterns of leveraging Databricks Apps for various business use cases. It can help users to leverage other Databricks-native services such as Serverless Compute,  Unity Catalog, Workflows,  Data Warehousing & Databricks SQL, Model Serving, and AI/BI Business Intelligence. 

Typically each Databricks App has three files:
- **requirements.txt** - list of the modules and packages required by the project.
- **app.yaml** 
	- A section name "command:" to list the command to be used to bootstrap the application
	- A section name "env:" to define environment variables as name-value pair (Optional)
- **app.py** - The the generic entry point of the applicaton  

This repository hosts the associated artifacts for the blog series. If you are new to the Databricks App, the you can start with flask-hello-world-app.

## Databricks Apps - Hands-on (1 of 3)
- **flask-hello-world-app**: 
	- It is a flask based simple "Hello, World!" web application
	
- **job-runner-app**: 
	 - A streamlit based web application that leverages Databricks Workflows to automate a BI reporting use case
     - The app accepts "Databricks job id" and additional text as parameters 
     - User triggers the the job based on the job id submited passing the parameters 
     - The project contains an example notebook to be used for the job    

## Databricks Apps - Hands-on (2 of 3)
Coming soon
## Databricks Apps - Hands-on (3 of 3)
Coming soon

## Contributors:

Souvik Pratiher & Purvang Parikh, 
Solution Architects, Databricks

If you find any bugs let us know by raising an issue!

