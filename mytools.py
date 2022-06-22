import requests

base_url = f"https://discord.com/api/v10"

header = {
    'Content-Type':'application/json',
    'authorization': 'TOKEN'
}

def getJson(url:str, param=None):
    full_url = f"{base_url}{url}"
    r = requests.get(full_url, params=param, headers=header)
    return r.json()

def postData(url, param=None):
    full_url = f"{base_url}{url}"
    r = requests.post(full_url, json=param, headers=header)
    return r.json()

def testPost(url):
    full_url = base_url+url
    data = {
        'recipient_id': 485515836707176458
    }
    r = requests.post(full_url, headers=header, json=data)
    return r.json()
