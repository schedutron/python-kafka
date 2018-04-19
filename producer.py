#producer.py

import time
import cv2
from kafka import SimpleProducer, KafkaClient

# connect to Kafka
kafka = KafkaClient('localhost:9092')
producer = SimpleProducer(kafka)

# Assign a topic
topic = 'Python'
