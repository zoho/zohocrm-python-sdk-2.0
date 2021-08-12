import threading

from zcrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
from zcrmsdk.src.com.zoho.api.authenticator.store import DBStore
from zcrmsdk.src.com.zoho.api.logger import Logger
from zcrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zcrmsdk.src.com.zoho.crm.api.initializer import Initializer
from zcrmsdk.src.com.zoho.crm.api.record import *
from zcrmsdk.src.com.zoho.crm.api.sdk_config import SDKConfig
from zcrmsdk.src.com.zoho.crm.api.user_signature import UserSignature


class MultiThread(threading.Thread):

    def __init__(self, module_api_name):
        super().__init__()
        self.module_api_name = module_api_name

    def run(self):
        print("Calling Get Records for module: " + self.module_api_name)
        response = RecordOperations().get_records(self.module_api_name)
        print(response)

    @staticmethod
    def call():
        log_instance = Logger.get_instance(Logger.Levels.INFO, "/Users/username/Documents/python_logs.txt")

        user = UserSignature("abc@zoho.com")

        token = OAuthToken("client_id", "client_secret", refresh_token="refresh_token")

        environment = USDataCenter.PRODUCTION()

        store = DBStore()

        resource_path = '/Users/username/Documents'

        sdk_config = SDKConfig(auto_refresh_fields=True, pick_list_validation=False)

        Initializer.initialize(user, environment, token, store, sdk_config, resource_path, log_instance)

        t1 = MultiThread('Leads')
        t2 = MultiThread('Deals')

        t1.start()
        t2.start()

        t1.join()
        t2.join()


# MultiThread.call()
