import boto3
import json


class KeyStore:
    def __init__(self, env="dev"):
        ssm = boto3.client('ssm')

        self.API_ACCESS_TOKEN = ssm.get_parameter(Name=f'/{env}/api/accessToken', WithDecryption=True)['Parameter']['Value']
        
        self.CREDIT_AUTH_TOKEN = ssm.get_parameter(Name=f'/{env}/shinigami/credit_auth_token', WithDecryption=True)['Parameter']['Value']
        self.API_HOST = ssm.get_parameter(Name=f'/{env}/api/host', WithDecryption=True)['Parameter']['Value']
        self.BUDDYDB_MONGO_DB_CONN_DETAILS = json.loads(
            ssm.get_parameter(Name=f'/{env}/DB/mongoDB/connectionDetails', WithDecryption=True)['Parameter']['Value'])
        self.CREDITRISKDB_MONGO_DB_CONN_DETAILS = json.loads(
            '{"db": "mongodb", "db_user": "creditriskdb-rwuser1", "db_password": "jO9Wl3wrqaXVgwh3", "host": "sp-prod-rs-shard-00-00-cy4kf.mongodb.net:27017,sp-prod-rs-shard-00-01-cy4kf.mongodb.net:27017,sp-prod-rs-shard-00-02-cy4kf.mongodb.net:27017", "db_name": "creditriskdb?ssl=true&ssl_cert_reqs=CERT_NONE&replicaSet=sp-prod-rs-shard-0&authSource=admin"}')
        self.REDSHIFT_DB_CONN_DETAILS = json.loads(
            ssm.get_parameter(Name=f'/{env}/DB/redshift/connectionDetails', WithDecryption=True)['Parameter']['Value'])

        # Collections
        self.YPRO_PRE_LOAN_DECISIONING_PARAMS_COLLECTION = "ypro_loan_decisioning_params"
        self.UNIQUE_DEVICE_PARAMETERS_COLLECTION = "unique_device_parameters"

        # APP related
        self.APP_NAME = "ypro_loan_decisioning_param_calculator"
