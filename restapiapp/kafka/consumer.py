from kafka import KafkaConsumer
import json

def get_consumer(topic, group_id):
    return KafkaConsumer(
        topic,
        bootstrap_servers="localhost:9092",
        group_id=group_id,
        value_deserializer=lambda v: json.loads(v.decode("utf-8"))
    )
