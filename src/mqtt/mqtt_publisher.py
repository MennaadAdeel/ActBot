import paho.mqtt.client as mqtt
import time

# Define broker address and port
broker_address = "o19fa16f.ala.us-east-1.emqxsl.com"
port = 1883
topic = "ActBot1234"

# Callback function for when the client receives a CONNACK response from the broker
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic)

# Callback function for when a PUBLISH message is received from the broker
def on_message(client, userdata, msg):
    print(f"Message received: {msg.payload.decode()} on topic {msg.topic}")

# Initialize MQTT client
client = mqtt.Client()

# Assign callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to broker
client.connect(broker_address, port, 60)

# Start the loop
client.loop_start()

# Function to publish blinking score and session score
def publish_scores(blinking_score, session_score):
    data = f"Blinking Score: {blinking_score}, Session Score: {session_score}"
    client.publish(topic, data)

