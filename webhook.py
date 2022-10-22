
import requests
import urllib.request
import json
from datetime import datetime

api = 'https://api.mir4.gq/v2/digest/server_join/182'
webhook = 'TOKEN'
response = urllib.request.urlopen(api)
obj = json.loads(response.read())
today = datetime.today()
dia = today.strftime("%d/%m | %H:%M")

data = {
        "username": "Entraram no Servidor",
        "content": ("<@&1027795709044465764>")
}

embedLines = ''

for line in obj:
        msgLine1 = "**__" 'Nick [' + line['name'] + "]__** **(" + line['class']['name'] + " " + line['power'] + ")**"
        msgLine2 = ''

        if "clan" in line['prior']:
                msgLine2 = 'Saiu [' + line['prior']['server']['name'] +'][' + line['prior']['clan']['name'] + '] e '
        else:
                msgLine2 = 'Desempacotou NFT e '

        if "clan" in line['current']:
                msgLine2 = msgLine2 + 'Entrou [' + line['current']['server']['name'] + '][' + line['current']['clan']['name'] + ']'
        else:
                msgLine2 = msgLine2 + 'Empacotou NFT'

        embedLines = embedLines + msgLine1 + '\n'
        embedLines = embedLines + msgLine2 + '\n'


data["embeds"] = [
        {
                "title": "**[SA2/SA62]**" " " + dia,
                "description": embedLines
        }
]


requests.post(webhook, json = data)
