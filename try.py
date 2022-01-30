import requests

payload = {
   'content': "!mine"
    
}

header = {

    'authorization': ''
}

r = requests.post("https://discord.com/api/v9/channels/923994324453179443/messages", data=payload, headers=header)