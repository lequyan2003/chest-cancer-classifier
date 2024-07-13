# chest-cancer-classifier

## Workflows
1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml

## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)

- [MLflow tutorial](https://youtube.com/playlist?list=PLkz_y24mlSJZrqiZ4_cLUiP0CBN5wFmTb&si=zEp_C8zLHt1DzWKK)

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

Run this to export as env variables: (`set` is used for Windows machines. For Linux or maxOS, use `export` instead)

```bash

set repo_owner=lequyan2003

set repo_name=chest-cancer-classifier

```

python script.py:

```bash

import dagshub
dagshub.init(repo_owner=repo_owner, repo_name=repo_name, mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)

```


### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag


## About MLflow & DVC

MLflow

 - Its Production Grade
 - Trace all of your experiments
 - Logging & tagging your model


DVC

 - Its very lite weight for POC only
 - lite weight experiments tracker
 - It can perform Orchestration (Creating Pipelines)

### Remember to manually create new folder `model` with file `model.h5` copied from artifacts directory

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	# with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws

	# Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2

	4. Pull Your image from ECR in EC2

	5. Launch your docker image in EC2

	# Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

  # Download Access keys:

	1. user > Security credentials

	2. Access keys > Create access key > CLI

    3. Download .csv file
	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 891377084283.dkr.ecr.us-east-2.amazonaws.com/chesty

	
## 4. Create EC2 machine (Ubuntu, t2.large, 2 last Allow ticks, 32GiB)

## 5. Open EC2 and Install docker in EC2 Machine:
	
	#optimal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    Settings>Actions>Runners>New self-hosted runner>Choose os Linux>Then run commands one by one
    (Enter the name of runner: self-hosted)


# 7. Setup github secrets:

    Settings>Secrets and variables>Actions>...
    
    AWS_ACCESS_KEY_ID =

    AWS_SECRET_ACCESS_KEY =

    AWS_REGION = us-east-2

    AWS_ECR_LOGIN_URI = demo>>  891377084283.dkr.ecr.us-east-2.amazonaws.com

    ECR_REPOSITORY_NAME = chesty

# 8. Connect

  Security>Security groups>Edit inbound rules>Add rule>Port range: 8080>0.0.0.0/0

  http://Public IPv4 address:8080
