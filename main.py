import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("AVIATION_STACK")


def getFlightInfo():

    params = {
        'access_key': API_KEY,
        'flight_iata': 'AF258',
        'limit': '1',
    }

    api_result = requests.get(
        'https://api.aviationstack.com/v1/flights', params)

    api_response = api_result.json()

    return api_response['data']


# for flight in api_response['results']:
#     if (flight['live']['is_ground'] is False):
#         print(u'%s flight %s from %s (%s) to %s (%s) is in the air.' % (
#             flight['airline']['name'],
#             flight['flight']['iata'],
#             flight['departure']['airport'],
#             flight['departure']['iata'],
#             flight['arrival']['airport'],
#             flight['arrival']['iata']))
