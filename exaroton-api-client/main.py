from exaroton_api_client import AuthenticatedClient as AC
from exaroton_api_client.api.server_actions import get_start_server as startServer
from exaroton_api_client.models.server import Server
import json

key = ""
with open("config.json", "r") as file:
    file = json.load(file)
    key = file['key']

client = AC(base_url="https://api.exaroton.com/v1/", token=key)


