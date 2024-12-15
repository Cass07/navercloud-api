import sys
import os
import requests
import time
import hmac
import hashlib
import base64

def __INIT__(self, api_base_url, api_uri, api_key, api_secret, method):
    self.api_base_url = api_base_url
    self.api_uri = api_uri
    self.api_key = api_key
    self.api_secret = api_secret
    self.method = method
    self.timestamp = str(int(time.time() * 1000))

def _make_signature(self):
    new_line = "\n"
    message = self.method + " " + self.api_uri + new_line + self.timestamp + new_line + self.api_key
    message = bytes(message, 'UTF-8')
    api_secret = bytes(self.api_secret, 'UTF-8')
    hmac_sha256 = base64.b64encode(hmac.new(api_secret, message, digestmod=hashlib.sha256).digest())
    return hmac_sha256

def _send_request(self):
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'X-ncp-apigw-timestamp': self.timestamp,
        'X-NCP-IAM-ACCESS-KEY': self.api_key,
        'X-NCP-APIGW-SIGNATURE-V2': self._make_signature(),
    }

    result = requests.get(self.api_base_url + self.api_uri, headers=headers).json()
    return result

def execute(self):
    return self._send_request()