from kafka import KafkaProducer

# Create Kafka producer instance
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # Kafka broker address
    value_serializer=lambda v: v.encode('utf-8')  # Convert string to bytes
)

# Send a few messages to the Kafka topic
for i in range(5):
    message = f"Message {i+1} from Python!"
    producer.send('my-topic', value=message)
    print(f"Sent: {message}")

# Close the producer connection
producer.close()
