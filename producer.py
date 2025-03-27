from kafka import KafkaProducer
from main import getFlightInfo

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # Kafka broker address
    value_serializer=lambda v: v.encode('utf-8')  # Convert string to bytes
)

flightInfo = getFlightInfo()[0]

if flightInfo['live'] is not None:
    message = f"Flight from {flightInfo['departure']['iata']} to {flightInfo['arrival']['iata']} \nAltitude: {flightInfo['live']['altitude']} \nSpeed: {flightInfo['live']['speed_horizontal']} \n Scheduled Arrival: {flightInfo['arrival']['scheduled']}"
else:
    message = f"Flight from {flightInfo['departure']['iata']} to {flightInfo['arrival']['iata']} \nCurrently not in-air."

producer.send('my-topic', value=message)
print(f"Sent: \n{message}")

producer.close()
