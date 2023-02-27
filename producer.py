# Import KafkaProducer from Kafka library
from kafka import KafkaProducer
import os

# Initialize producer variable and set parameter for txt encode

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: str(x).encode('utf-8'))

with open('/Users/asthapatwa/Downloads/kafka_2.12-3.4.0/python_assignment/files/readdata.txt', mode='r') as f:
    data = f.readline()
    producer.send('test', value=data)

producer.flush()
 
# Print message
print("Message Sent")
