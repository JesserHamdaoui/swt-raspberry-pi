import requests

def get_current_position(ip):
    response = requests.get(ip + 'api/currentPosition')
    if response.status_code == 200:
        return response.json()
    else:
        return response.content

