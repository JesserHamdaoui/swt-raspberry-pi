import requests

def post_currentStatus(ip, windSpeed, windDirection, generatedEnergy, staticEnergy, consumedEnergy, alerts):
    data = {
        "windSpeed": windSpeed,
        "windDirection": windDirection,
        "generatedEnergy": generatedEnergy,
        "staticEnergy": staticEnergy,
        "consumedEnergy": consumedEnergy,
        "alerts": alerts
    }

    response = requests.post(ip + 'api/currentStatus', json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return response.status_code
