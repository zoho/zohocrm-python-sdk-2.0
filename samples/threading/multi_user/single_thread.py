from zcrmsdk.src.com.zoho.crm.api.user_signature import UserSignature
from zcrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
from zcrmsdk.src.com.zoho.api.authenticator.store import DBStore
from zcrmsdk.src.com.zoho.api.logger import Logger
from zcrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zcrmsdk.src.com.zoho.crm.api.initializer import Initializer
from zcrmsdk.src.com.zoho.crm.api.record import *
from zcrmsdk.src.com.zoho.crm.api.sdk_config import SDKConfig
from zcrmsdk.src.com.zoho.crm.api.user_signature import UserSignature


class SingleThread(object):

    def __init__(self, environment, token, user, module_api_name, sdk_config):
        self.environment = environment
        self.token = token
        self.user = user
        self.module_api_name = module_api_name
        self.sdk_config = sdk_config

    def run(self):
        try:
            Initializer.switch_user(self.user, self.environment, self.token, self.sdk_config)

            print('Getting records for User: ' + Initializer.get_initializer().user.email)

            response = RecordOperations().get_records(self.module_api_name)

            print(response)

        except Exception as e:
            print(e)

    @staticmethod
    def call():
        log_instance = Logger.get_instance(Logger.Levels.INFO, "/Users/username/Documents/python_logs.txt")

        user1 = UserSignature("abc@zoho.com")

        token1 = OAuthToken("client_id", "client_secret", refresh_token="refresh_token")

        environment = USDataCenter.PRODUCTION()

        store = DBStore()

        resource_path = '/Users/username'

        user1_module_api_name = 'Leads'

        user2_module_api_name = 'Contacts'

        user2 = UserSignature("abc@zoho.com")

        token2 = OAuthToken("client_id", "client_secret", refresh_token="refresh_token")

        sdk_config_1 = SDKConfig(auto_refresh_fields=True, pick_list_validation=False)

        sdk_config_2 = SDKConfig(auto_refresh_fields=False, pick_list_validation=False)

        Initializer.initialize(user1, environment, token1, store, sdk_config_1, resource_path, log_instance)

        single_thread = SingleThread(environment, token1, user1, user1_module_api_name, sdk_config_1)
        single_thread.run()

        single_thread = SingleThread(environment, token2, user2, user2_module_api_name, sdk_config_2)
        single_thread.run()


# SingleThread.call()
