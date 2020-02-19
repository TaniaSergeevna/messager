import requests
import os

print("Enter username:")
username = input()

print("Enter password:")
password = input()

while True:
    text = input("Enter message:")

    os.system('cls' if os.name == 'nt' else 'clear')

    response = requests.post(
        'http://127.0.0.1:5000/send',
        json={
            "username": username,
            "password": password,
            "text": text
        }
    )

    if not response.json()['ok']:
        print('Access denied')
        break

