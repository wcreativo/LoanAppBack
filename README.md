<!--
title: 'Serverless Python Flask API on AWS'
description: 'Interview exercise'
layout: Doc
framework: v3
platform: AWS
language: Python
priority: 2
-->

# LoanApp - Serverless Python Flask API on AWS

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

```bash
python3.9 -m venv ./venv
source ./venv/bin/activate
```

```bash
pip install -r requirements.txt
flask run
```

### Endpoint

Post
```bash
https://6heqmtw8dg.execute-api.us-east-2.amazonaws.com/loan/
```

Request example:
```bash
{
    "amount": 5000,
    "tax_id": "5654-565",
    "business_name": "Embyter"
}
```

### Testing

```bash
python3.9 -m venv ./venv
pip install -r requirements.txt
pytest
```