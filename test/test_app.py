import uuid
from app.business import app
from unittest import TestCase
from fastapi.testclient import TestClient
from cloudevents.http import CloudEvent, to_binary, to_structured

class Test(TestCase):
      def test_service_process(self):

        name_test = "name test"
        client = TestClient(app.app)
        attributes = {
          "id": str(uuid.uuid4()),
          "specversion": "0.3",
          "source": "knative/eventing/samples/hello-world",
          "type" : "dev.knative.samples.hifromknative"
        }
        data = {"msg": name_test}

        event = CloudEvent(attributes, data)
        headers, body = to_binary(event)
        response = client.post("/",headers=headers, data=body)
        print("response: "+str(response.json()))

        self.assertEqual(str(name_test), response.json()['msg'])

