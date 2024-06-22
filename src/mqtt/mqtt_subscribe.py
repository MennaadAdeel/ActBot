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
    process_received_message(msg.payload.decode())

def process_received_message(message):
    print(f"Message received: {message}")
    # Extract session information from the message and handle accordingly
    # Assuming message format: "Child: <child_name>, Session: <session_count>"
    parts = message.split(", ")
    child_name = parts[0].split(": ")[1]
    session_count = int(parts[1].split(": ")[1])
    handle_session_info(child_name, session_count)

def handle_session_info(child_name, session_count):
    print(f"Handling session info for {child_name} with session count {session_count}")
    # Implement the logic to handle the session information
    # For example, you might log this information or trigger some actions on the robot

# Function to initialize and start the MQTT subscriber
def start_mqtt_subscriber():
    client = mqtt.Client()

    # Assign callback functions
    client.on_connect = on_connect
    client.on_message = on_message

    # Connect to broker
    client.connect(broker_address, port, 60)

    # Start the loop
    client.loop_start()
    return client


