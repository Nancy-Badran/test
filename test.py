from flask import Flask, jsonify
app = Flask(__name__)
from flask import request
from flask import json
from time import gmtime, strftime
import datetime

payload = [
   {
  "id": "cb8c3971-9adc-488b-xxxx-43cbb4974ff5",
  "timestamp": "2017-11-17T16:52:01.343145347Z",
  "action": "push",
  "target": {
    "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
    "size": 524,
    "digest": "sha256:xxxxd5c8786bb9e621a45ece0dbxxxx1cdc624ad20da9fe62e9d25490f33xxxx",
    "length": 524,
    "repository": "hello-world",
    "tag": "v1"
  },
  "request": {
    "id": "3cbb6949-7549-4fa1-xxxx-a6d5451dffc7",
    "host": "myregistry.azurecr.io",
    "method": "PUT",
    "useragent": "docker/17.09.0-ce go/go1.8.3 git-commit/afdb6d4 kernel/4.10.0-27-generic os/linux arch/amd64 UpstreamClient(Docker-Client/17.09.0-ce \\(linux\\))"
  }
}
]
@app.route('/webhook', methods = ['POST'])
def api_message():

  

    if request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)

    elif request.headers['Content-Type'] == 'text/plain':
        now = datetime.datetime.now()
        timestamp = str(now.strftime("%Y%m%d_%H:%M:%S"))
        filename = "webhook-" + timestamp + ".json"
        file = open(filename,"w") 
        file.write()
        file.close()
        return "Binary message written!"

    else:
        return "415 Unsupported Media Type ;)"
app.run()
