from zcrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
from zcrmsdk.src.com.zoho.api.authenticator.store import FileStore
from zcrmsdk.src.com.zoho.api.logger import Logger
from zcrmsdk.src.com.zoho.crm.api import SDKConfig
from zcrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zcrmsdk.src.com.zoho.crm.api.initializer import Initializer
from zcrmsdk.src.com.zoho.crm.api.user_signature import UserSignature


class SDKInitializer(object):
    @staticmethod
    def initialize_sdk():
        """
        Create an instance of Logger Class that takes two parameters
        1 -> Level of the log messages to be logged. Can
        be configured by typing Levels "." and choose any level from the list displayed.
        2 -> Absolute file path, where messages need to be logged.
        """
        log_instance = Logger.get_instance(Logger.Levels.INFO, "/Users/username/Documents/python_logs.txt")

        # Create an UserSignature instance that takes user Email as parameter
        user = UserSignature("abc@zoho.com")

        # Create a Token instance

        """
        Create a Token instance that takes the following parameters
        1 -> OAuth client id.
        2 -> OAuth client secret.
        3 -> OAuth redirect URL.
        4 -> OAuth refresh token.
        5 -> token type.
        """
        token = OAuthToken("client_id", "client_secret", refresh_token="refresh_token")

        # Configure the environment
        # which is of the pattern Domain.Environment
        # Available Domains: USDataCenter, EUDataCenter, INDataCenter, CNDataCenter, AUDataCenter
        # Available Environments: PRODUCTION(), DEVELOPER(), SANDBOX()
        environment = USDataCenter.PRODUCTION()

        # Create an instance of TokenStore
        """
        Create an instance of TokenStore
        1 -> Absolute file path of the file to persist tokens
        """
        """
        Create an instance of TokenStore
        1 -> DataBase host name. Default value "localhost"
        2 -> DataBase name. Default value "zohooauth"
        3 -> DataBase user name. Default value "root"
        4 -> DataBase password. Default value ""
        5 -> DataBase port number. Default value "3306"
        """
        # store = DBStore()
        store = FileStore('/Users/username/Documents/python_tokens.txt')

        """
         A Boolean value for the key (auto_refresh_fields) to allow or prevent auto-refreshing of the modules' 
         fields in the background.
         if true - all the modules' fields will be auto-refreshed in the background whenever there is any change.
		 if false - the fields will not be auto-refreshed in the background. 
		 The user can manually delete the file(s) or the specific module's fields using methods from ModuleFieldsHandler
        """
        config = SDKConfig(auto_refresh_fields=True, pick_list_validation=False)

        """The path containing the absolute directory path (in the key resource_path) to store user-specific files 
        containing information about fields in modules. """
        resource_path = '/Users/username/Documents'

        """
        Call the static initialize method of Initializer class that takes the following arguments
         1 -> UserSignature instance
         2 -> Environment instance
         3 -> Token instance
         4 -> TokenStore instance
         5 -> Logger instance
         6 -> auto_refresh_fields
         7 -> resource_path
        """
        Initializer.initialize(user, environment, token, store, config, resource_path, log_instance)
