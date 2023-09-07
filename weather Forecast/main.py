API_KEY = "228e2317036b152d20c06e537dbbfeaf"
import requests
import random
from twilio.rest import Client

parameters = {
    "lon": random.randint(-10000,10000)/random.randint(-100,100),
    "lat": random.randint(-1000,1000)/random.randint(-100,100),
    "appid":API_KEY
}
response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
weather_id = data["weather"][0]["id"]
print(weather_id)
if weather_id < 800:
    print("Rain!")
    account_sid = "AC3897f3470f270a0e6dd5b1993491b544"
    auth_token = "9033f5dca0fee7470a472ec1b3d32f85"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It might rain today, carry an umbrella!",
        from_="+12536428755",
        to="+919060791307"
    )

else:
    print("Nothing ")
    account_sid = "AC3897f3470f270a0e6dd5b1993491b544"
    auth_token = "9033f5dca0fee7470a472ec1b3d32f85"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Nothing to worry today!",
        from_="+12536428755",
        to="+919060791307"
    )