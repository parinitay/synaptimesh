import paho.mqtt.client as mqtt
from backend.config import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC

client = mqtt.Client()

def connect_mqtt():
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    print("MQTT Connected")

def publish_command(command):
    client.publish(MQTT_TOPIC, command)
    print(f"Published: {command}")