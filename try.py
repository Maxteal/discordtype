import requests
from time import sleep

count = 0



while count < 5:


    payload = {
        'content': "!mine"
}

    header = {
        'authorization': 'Your token here'
}

    r = requests.post("https://discord.com/api/v9/channels/923994324453179443/messages", data=payload, headers=heade>


    sleep(3)
