import json
import uuid
import os
import requests
import logging
from cloudevents.http import CloudEvent, to_binary, from_http
from app.models.cloud_event_model import CloudEventModel
from fastapi import FastAPI, Request, Response

# this is a basic configuration for a log file
logging.basicConfig(
    filename='business_app.log',
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

# Levels of logs:
# DEBUG: Detailed information, typically of interest only when diagnosing problems.
# INFO: Confirmation that things are working as expected.
# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# Example:
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.error('This is an error message')

app = FastAPI()

@app.post("/")
async def service_process(event_received: CloudEventModel, request: Request, response: Response):

    k_sink = os.environ.get('K_SINK', '')

    logging.info(event_received.dict())
    logging.info(event_received.msg)

    # for this example, the parameter msg is required
    if event_received.msg == None:
        response.status_code = 400
        logging.error("Bad Request: msg parameter not found.")
        return "msg parameter not found."

    data = {"msg": "Hi - " + event_received.msg}

    try:
        # it is validated that the event is correct
        from_http(request.headers,json.dumps(event_received.dict()))
        logging.debug("Event received successfully")
    except Exception as ex:
        logging.error("headers: type and source are required.")
        return {"msg": "headers: type and source are required."}

    # create a new CloudEvent
    new_event = from_http(
        {
           "Content-Type":"application/json",
           "ce-specversion": "0.3",
           "ce-id":str(uuid.uuid4()),
           "ce-type": "dev.knative.samples.hifromknative",
           "ce-source": "knative/eventing/samples/hello-world"
        },
        json.dumps(data)
    )
    headers, body = to_binary(new_event)

    # Respond with another event (optional)
    if k_sink != '':
       r = requests.post(k_sink,headers=headers, data=body)
       logging.info(r.status_code)

    logging.debug('Response: '+ str(data))
    return data
