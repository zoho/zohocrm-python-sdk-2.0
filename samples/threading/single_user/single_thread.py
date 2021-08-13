from zcrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
from zcrmsdk.src.com.zoho.api.authenticator.store import DBStore
from zcrmsdk.src.com.zoho.api.logger import Logger
from zcrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zcrmsdk.src.com.zoho.crm.api.initializer import Initializer
from zcrmsdk.src.com.zoho.crm.api.record import *
from zcrmsdk.src.com.zoho.crm.api.sdk_config import SDKConfig
from zcrmsdk.src.com.zoho.crm.api.user_signature import UserSignature


class SingleThread():

    @staticmethod
    def call():
        log_instance = Logger.get_instance(Logger.Levels.INFO, "/Users/username/Documents/python_logs.txt")

        user = UserSignature("abc@zoho.com")

        token = OAuthToken("client_id", "client_secret", refresh_token="refresh_token")

        environment = USDataCenter.PRODUCTION()

        store = DBStore()

        resource_path = '/Users/username'

        sdk_config = SDKConfig(auto_refresh_fields=True, pick_list_validation=False)

        Initializer.initialize(user, environment, token, store, sdk_config, resource_path, log_instance)

        module_1 = "Leads"

        module_2 = "Contacts"

        response_1 = RecordOperations().get_records(module_1)

        response_2 = RecordOperations().get_records(module_2)

# SingleThread.call()
