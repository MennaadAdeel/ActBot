import paho.mqtt.client as mqtt

# Define the broker address and port
broker_address = "broker.emqx.io"
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
client.loop_forever()
