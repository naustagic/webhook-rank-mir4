# from mir4_webhook import objects
import json

import requests

from mir4_webhook.objects import Guild


class MirAPI:
    base_url: str = "https://api.mir4.gq/v1/clan/52289808/roster/"

    def __init__(self, roster: str = "32"):
        self.url = self.base_url + roster

    def request(self):
        url = self.url
        response = requests.get(url)
        data = response.json()

        return Guild.from_dict(data)
