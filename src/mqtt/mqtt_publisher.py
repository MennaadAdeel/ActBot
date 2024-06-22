import paho.mqtt.client as mqtt
import time

# Define broker address and port
broker_address = "o19fa16f.ala.us-east-1.emqxsl.com"  # Use the IP address if accessing remotely
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

try:
    while True:
        # Your data to be sent
        data = "Hello from Raspberry Pi!"

        # Publish data to the topic
        client.publish(topic, data)

        # Sleep for some time before publishing next message
        time.sleep(5)  # 5 seconds interval

except KeyboardInterrupt:
    # Disconnect from MQTT broker
    client.disconnect()
    client.loop_stop()
