# lamnda-seed-python
***
## Description:
A simple web app written in Python. It shows how to consume a [CloudEvent](https://cloudevents.io/) in Knative eventing, and optionally how to respond back with another CloudEvent in the http response, by adding the Cloud Eventing headers outlined in the Cloud Events standard definition.

***
## Run Locally
To run the commands you must be on the root of the repository


### Local execution
🚨 NOTE: You must be having installed python3.7 or higher in your local machine
### LINUX:
``python -m venv venv``

``./venv/bin/activate``

``pip install --no-cache-dir -r requirements.txt``

``uvicorn app.business.app:app --reload --port [port number]``
### WINDOWS:
``python -m venv venv``

``.\venv\Scripts\activate``

``pip install --no-cache-dir -r requirements.txt``

``uvicorn app.business.app:app --reload --port [port number]``

this will start the server to the default host: http://127.0.0.1:[port number]

you can see the swagger documentations in: http://127.0.0.1:[port number]/docs

***

## Try the api

1. To try the api running in local run, execute following command in the SSH terminal:

    ```bash
    curl -v "http://127.0.0.1:8000/" \
    -X POST \
    -H "Ce-Id: 536808d3-88be-4077-9d7a-a3f162705f79" \
    -H "Ce-specversion: 0.3" \
    -H "Ce-Type: dev.knative.samples.helloworld" \
    -H "Ce-Source: dev.knative.samples/helloworldsource" \
    -H "Content-Type: application/json" \
    -d '{"msg": "seed python"}'
    exit
    ```
***

## For unittest
To run the unittest and coverage run the next commands:

``coverage run -m unittest discover``

`` coverage html -d coverage_html``

after run the last command you can find a folder with the name "coverage html" open the index.html file inside and filter by "app/" for show only the app coverage