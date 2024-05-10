from tools.post_log import post_log
from tools.post_currentStatus import post_currentStatus
from tools.post_report import post_report
from tools.get_current_position import get_current_position
from tools.get_weather_data import get_weather_data
from tools.ServoMotor import ServoMotor
from time import sleep
from datetime import datetime
from math import pi, cos
import requests
import geocoder
import RPi.GPIO as GPIO

ip = "http://172.20.10.3:5000/"
wind_turbine_direction = get_current_position(ip)['currentAngle']
lat, lng = geocoder.ip('me').latlng
wind_turbine = {"location": {"lat": lat,"long": lng},"_id": "wt-3l3kl21","height": 0.4,"bladesLength": 0.2, "staticDirection": wind_turbine_direction}

servo = ServoMotor(18, 0)
print(wind_turbine)

air_density = 1.3
coefficient_of_performance = 0.5

raspi_power = 3
servo_power = 4.8 * 1.2

delta_time = 60

while True:
    try:
        weather_data = get_weather_data()
        print(weather_data)
        wind_direction = weather_data['wind_direction']
        wind_speed = weather_data['wind_speed']
        date_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.000Z')
        print(date_time)
        angle_of_attack = abs(wind_direction - wind_turbine_direction)
        
        post_log(ip, wind_turbine, date_time, wind_direction, angle_of_attack, wind_speed, "Turn")
        
        # Turn the servo motor to the desired angle
        servo.turn(wind_direction)
        
        # Generated energy
        generated_energy = 0.5 * coefficient_of_performance * air_density * pi * (wind_turbine["bladesLength"]**2) * (wind_speed ** 3) * delta_time
        
        # Static energy
        static_energy = 0.5 * coefficient_of_performance * air_density * pi * (wind_turbine["bladesLength"]**2) * ((wind_speed * abs(cos(angle_of_attack)) )** 3) * delta_time 
        
        # consumed energy
        consumed_energy = (servo_power + raspi_power) * delta_time
        
        print(generated_energy, static_energy, consumed_energy)
                
        # post to current status
        post_currentStatus(ip, wind_speed, wind_direction, generated_energy, static_energy, consumed_energy, [])
        
        # post to report
        post_report(ip, date_time, generated_energy, static_energy, consumed_energy)
        
        sleep(60)
        
    except KeyboardInterrupt:
        print("Stop")
        break


