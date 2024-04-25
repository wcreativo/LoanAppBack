<!--
title: 'Serverless Python Flask API on AWS'
description: 'Interview exercise'
layout: Doc
framework: v3
platform: AWS
language: Python
priority: 2
-->

# LoanAPP - Serverless Python Flask API on AWS

This document demostrates how to develop and deploy LoanApp project, running on AWS Lambda using Serverless Framework.


## Usage

### Prerequisites

In order to package your dependencies locally with `serverless-python-requirements`, you need to have `Python3.9` installed locally. You can create and activate a dedicated virtual environment with the following command:

```bash
python3.9 -m venv ./venv
source ./venv/bin/activate
```

Alternatively, you can also use `dockerizePip` configuration from `serverless-python-requirements`. For details on that, please refer to corresponding [GitHub repository](https://github.com/UnitedIncome/serverless-python-requirements).

### Deployment

In order to deploy with dashboard, you need to first login with:

```
serverless login
```

install dependencies with:

```
npm install
```

and then perform deployment with:

```
serverless deploy
```

### Local development

Thanks to capabilities of `serverless-wsgi`, it is also possible to run your application locally, however, in order to do that, you will need to first install `werkzeug`, `boto3` dependencies, as well as all other dependencies listed in `requirements.txt`. It is recommended to use a dedicated virtual environment for that purpose. You can install all needed dependencies with the following commands:

```bash
pip install werkzeug boto3
pip install -r requirements.txt
flask run
```

### Tech Stack

- TDD
- Flask
- Pydantic
