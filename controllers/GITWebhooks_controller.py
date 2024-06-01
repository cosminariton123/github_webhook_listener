from my_framework.my_http.base_controller import BaseController
from my_framework.my_http.http_data_types import HttpResponse
from verify_signature import verify_signature
from dtos.message import Message
from config import ACTION, SECRET_TOKEN

import json

class GITWebhooksController(BaseController):
    def __init__(self):
        base_path="/GITWebhooks"
        super().__init__(base_path)
        
        self.methods_dict["post_update"] += "/update"

    def post_update(self, http_request):        
        body = http_request.body

        if "X-Hub-Signature-256" not in http_request.headers:
            return HttpResponse(403, {}, Message("X-Hub-Signature-256 header is missing!"))

        if verify_signature(body, SECRET_TOKEN, http_request.headers["X-Hub-Signature-256"]) is False:
            return HttpResponse(403, {}, Message("Request signatures didn't match!"))


        body = json.loads(body)

        action = body["action"]
        merged = body["pull_request"]["merged"]
        ref = body["pull_request"]["base"]["ref"]

        if action == "closed" and merged == True and (ref == "main" or ref == "master"):
            ACTION()
        
        response_body = ""
        response = HttpResponse(200, {}, response_body)
        return response
