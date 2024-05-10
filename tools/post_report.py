import requests

def post_report(ip, dateTime, energyGenerated, energyConsumption, staticEnergy):
    
    data = {"dateTime": dateTime, "series": [{"name": "Energy Generated", "data": energyGenerated}, {"name": "Energy Consumption", "data": energyConsumption}, {"name": "Static Energy Generated", "data": staticEnergy}]}
    
    response = requests.post(ip + 'api/report', json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return response.status_code
