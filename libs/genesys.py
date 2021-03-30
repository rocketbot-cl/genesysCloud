import json
import base64
import pprint
import os
from datetime import datetime

from PureCloudPlatformClientV2.api_client import ApiClient
from PureCloudPlatformClientV2.rest import RESTClientObject
from PureCloudPlatformClientV2.apis import *


class GenesysCloud:
    
    def __init__(self, client_id, client_secret, auth_code=None, redirect_uri=None,):
        self.api_client = ApiClient()
        self.client_id = client_id
        self.client_secret = client_secret
        self.auth_code = auth_code
        self.redirect_uri = redirect_uri
        self.auth_token = None
        self.expires_in = "01/01/1970"
        self.authorized = False
        self.client = None

    def authorize(self, path, session=None):
        if session is None:
            session = "default"

        config_file = path + session + ".json"
        self._read_config(config_file)

        if self.is_expired():
            if not self.authorized:
                self.api_client, response = self.api_client.get_code_authorization_token(
                    self.client_id, self.client_secret, self.auth_code, self.redirect_uri)
            else:
                self.api_client, response = self.api_client.refresh_code_authorization_token(
                    self.client_id, self.client_secret, self.refresh_token)

            response["authorized"] = True
            self.expires_in = response["expires_in"]
            self._create_config(config_file, response)

        return self.api_client

    def _read_config(self, config_file):
        if os.path.exists(config_file):
            with open(config_file, 'r') as json_file:
                data = json.load(json_file)
            
            self.authorized = data["authorized"]
            self.refresh_token = data["refresh_token"]

    def _create_config(self, config_file, response):
        expires_in = response["expires_in"]
        response["expires_in"] = self._get_expires_date(expires_in).strftime("%d/%m/%Y")
        
        with open(config_file, 'w') as outfile:
            json.dump(response, outfile)

    def _get_expires_date(self, timestamp):
        now = datetime.timestamp(datetime.now())
        expires_in = timestamp + now
        return datetime.fromtimestamp(expires_in)

    def is_expired(self):
        expires_date = datetime.strptime(self.expires_in, "%d/%m/%Y")
        delta = datetime.now() - expires_date
        return True if delta.days >= 1 else False



