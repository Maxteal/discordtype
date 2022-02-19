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

    r = requests.post("Your Channel Here", data=payload, headers=header>


    sleep(3)
