import random
import requests
import time
import urllib.parse
import json
import base64
import socket
from datetime import datetime



headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9',
    'Content-Type': 'application/json',
    'Origin': 'https://major.glados.app',
    'Priority': 'u=1, i',
}


def load_credentials():
    try:
        with open('query_id.txt', 'r') as f:
            queries = [line.strip() for line in f.readlines()]
        return queries
    except FileNotFoundError:
        print("File query_id.txt tidak ditemukan.")
        return [  ]
    except Exception as e:
        print("Terjadi kesalahan saat memuat token:", str(e))
        return [  ]

def getuseragent(index):
    try:
        with open('useragent.txt', 'r') as f:
            useragent = [line.strip() for line in f.readlines()]
        if index < len(useragent):
            return useragent[index]
        else:
            return "Index out of range"
    except FileNotFoundError:
        return 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36'
    except Exception as e:
        return 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36'

def postauth(query):
    url = 'https://major.glados.app/api/auth/tg/'
    data = {
        'init_data': query,
    }
    try:
        response_codes_done = range(200, 211)
        response_code_failed = range(500, 530)
        response_code_notfound = range(400, 410)
        response = requests.post(url, headers=headers, json=data)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_failed:
            print(response.text)
            return None
        elif response.status_code in response_code_notfound:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None
    
def getdaily(token):
    url ='https://major.glados.app/api/tasks/?is_daily=true'
    headers['Authorization'] = f"Bearer {token}"
    try:
        response_codes_done = range(200, 211)
        response_code_failed = range(500, 530)
        response_code_notfound = range(400, 410)
        response = requests.get(url, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_failed:
            print(response.text)
            return None
        elif response.status_code in response_code_notfound:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def gettask(token):
    url ='https://major.glados.app/api/tasks/?is_daily=false'
    headers['Authorization'] = f"Bearer {token}"
    try:
        response_codes_done = range(200, 211)
        response_code_failed = range(500, 530)
        response_code_notfound = range(400, 410)
        response = requests.get(url, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_failed:
            print(response.text)
            return None
        elif response.status_code in response_code_notfound:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def donetask(token, id):
    url = 'https://major.glados.app/api/tasks/'
    headers['Authorization'] = f"Bearer {token}"
    payload = {
        'task_id': id
    }
    try:
        response_codes_done = range(200, 211)
        response_code_failed = range(500, 530)
        response_code_notfound = range(400, 410)
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_failed:
            print(response.text)
            return None
        elif response.status_code in response_code_notfound:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def visit(token):
    url = 'https://major.glados.app/api/user-visits/visit/?'
    headers['Authorization'] = f"Bearer {token}"
    try:
        response_codes_done = range(200, 211)
        response_code_failed = range(500, 530)
        response_code_notfound = range(400, 410)
        response = requests.post(url, headers=headers)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_failed:
            print(response.text)
            return None
        elif response.status_code in response_code_notfound:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None
    
def donate(token, amount):
    url = 'https://major.glados.app/api/invoices/'
    payload = {"amount":amount, 
               "buy_for_user_id":6057140648}
    headers['Authorization'] = f"Bearer {token}"
    try:
        response_codes_done = range(200, 211)
        response_code_failed = range(500, 530)
        response_code_notfound = range(400, 410)
        response = requests.post(url, headers=headers, json=payload)
        print(response.text)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_failed:
            print(response.text)
            return None
        elif response.status_code in response_code_notfound:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def roulette(token):
    url ='https://major.glados.app/api/roulette?'
    headers['Authorization'] = f"Bearer {token}"

    response = requests.post(url, headers=headers)
    try:
        response_codes_done = range(200, 211)
        response_code_failed = range(500, 530)
        response_code_notfound = range(400, 410)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_failed:
            print(response.text)
            return None
        elif response.status_code in response_code_notfound:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def join_squad(token):
    url = 'https://major.glados.app/api/squads/2139244595/join/?'
    headers['Authorization'] = f"Bearer {token}"

    response = requests.post(url, headers=headers)
    try:
        response_codes_done = range(200, 211)
        response_code_failed = range(500, 530)
        response_code_notfound = range(400, 410)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_failed:
            print(response.text)
            return None
        elif response.status_code in response_code_notfound:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def get_squad(token):
    url = 'https://major.glados.app/api/squads/2139244595?'
    headers['Authorization'] = f"Bearer {token}"

    response = requests.get(url, headers=headers)
    try:
        response_codes_done = range(200, 211)
        response_code_failed = range(500, 530)
        response_code_notfound = range(400, 410)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_failed:
            print(response.text)
            return None
        elif response.status_code in response_code_notfound:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def main():
    while True:
        queries = load_credentials()
        for index, query in enumerate(queries):
            useragent = getuseragent(index)
            headers['User-Agent'] = useragent
            print(f"========== Account {index+1} ==========")
            time.sleep(1)
            data_auth = postauth(query)
            print(f"refresh token....")
            time.sleep(2)
            if data_auth is not None:
                token = data_auth.get('access_token')
                user = data_auth.get('user')
                ratings = user.get('rating')
                squad_id = user.get('squad_id')
                print(squad_id)
                print(f"TGID : {user.get('id')} | Name : {user.get('first_name')} {user.get('last_name')} | point : {ratings}")

                time.sleep(2)
                if squad_id == None:
                    print('No Have Squad')
                    time.sleep(2)
                    print('Joining Squad....')
                    time.sleep(2)
                    data_squad = join_squad(token)
                    if data_squad is not None:
                        print("Join Squad Done")
                else:
                    data_squad = get_squad(token)
                    if data_squad is not None:
                        print(f"Squad : {data_squad.get('name')} | Member : {data_squad.get('members_count')} | Ratings : {data_squad.get('rating')}")

                time.sleep(1)
                data_visit = visit(token)
                if data_visit is not None:
                    print(f"Login Streak : {data_visit.get('streak')}")
                    time.sleep(2)
                

                print("Spin Roulette")
                data_roulette = roulette(token)
                if data_roulette is not None:
                    reward = data_roulette.get('rating_award')
                    if reward is not None:
                        print(f"Reward Roulette : {data_roulette.get('rating_award')}")
                    else:
                        print("Reward Roulette Claimed....")
                time.sleep(3)
                print('Get daily Task')
                data_daily = getdaily(token)
                if data_daily is not None:
                    if len(data_daily) > 0:
                        if len(data_daily) > 3:
                            elements = data_daily.pop(4)
                            data_daily.insert(0, elements)
                        for daily in data_daily:
                            id = daily.get('id')
                            time.sleep(2)
                            data_done = donetask(token, id)
                            title = daily.get('title')
                            if title not in ["Donate rating", "Invite more Friends", "Boost channel"]:
                                if data_done is not None:
                                    print(f"Task : {daily.get('title')} | Reward : {daily.get('award')} | Status: {data_done.get('is_completed')}")
                    else:
                        print('No have daily task')

                print('Get Single Task')
                data_task = gettask(token)
                if data_task is not None:
                    if len(data_task) > 0:
                        for task in data_task:
                            id = task.get('id')
                            time.sleep(2)
                            data_done = donetask(token, id)
                            if data_done is not None:
                                print(f"Task : {task.get('title')} | Reward : {task.get('award')} | Status: {data_done.get('is_completed')}")
                    else:
                        print('No have single task')
                time.sleep(3)
                # if index != 0:
                #     if ratings >= 2500:
                #         amount = 2500
                #     elif ratings >= 1000:
                #         amount = 1000
                #     elif ratings >= 500:
                #         amount = 500
                #     elif ratings >= 250:
                #         amount = 250
                #     else:
                #         amount = 100
                #     data_donate = donate(token, amount)
                #     if data_donate is not None:
                #         print(f"Donate amount {amount}")
            else:
                print('User Not Found')
        delay = random.randint(28000, 28500)
        printdelay(delay)
        time.sleep(delay)

def printdelay(delay):
    now = datetime.now().isoformat(" ").split(".")[0]
    hours, remainder = divmod(delay, 3600)
    minutes, sec = divmod(remainder, 60)
    print(f"{now} | Waiting Time: {hours} hours, {minutes} minutes, and {sec} seconds")

if __name__ == "__main__":
    main()
