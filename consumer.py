from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'my-topic',  # Kafka topic name
    bootstrap_servers='localhost:9092',  # Kafka broker address
    auto_offset_reset='earliest',  # Start reading from the beginning
    group_id='my-group'  # Consumer group
)

print("Waiting for messages...")
for message in consumer:
    print(f"Received: {message.value.decode('utf-8')}")
