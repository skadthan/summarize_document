from kafka import KafkaProducer

import json

producer = KafkaProducer(
    bootstrap_servers="localhost:29092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def publish_event(topic, message):
    print("publish_event: ", topic, message)
    producer.send(topic, message)
    producer.flush()
