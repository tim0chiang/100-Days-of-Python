import requests
from twilio.rest import Client

api_key = 'example'

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
CHECKING_HOURS = 12
account_sid = 'AC9ee8e5c0058af860b6a5752774711051'
auth_token = '004208410693fe3062867084a5b6b20c'

weather_parameters = {
    'lat': 49.219608,
    'lon': -122.908463,
    'appid': api_key,
    'exclude': 'minutely,daily,current'
}


response = requests.get(OWM_Endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()


all_hours = weather_data['hourly'][:CHECKING_HOURS]

all_conditions = [data['weather'][0]['id'] for data in all_hours if data['weather'][0]['id'] < 700]

if len(all_conditions) != 0:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember bring an ☔",
        from_='+15204369954',
        to='778-882-7017'
    )
    print(message.status)
