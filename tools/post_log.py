import requests

def post_log(ip, windTurbine, dateTime, windDirection, angleOfAttack, windSpeed, status):

    data = {
        "windTurbine": windTurbine,
        "dateTime": dateTime,
        "windDirection": windDirection,
        "angleOfAttack": angleOfAttack,
        "windSpeed": windSpeed,
        "status": status
    }
    response = requests.post(ip + 'api/log', json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return response.status_code
