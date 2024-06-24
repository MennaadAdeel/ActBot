from src.mqtt.mqtt_subscribe import start_mqtt_subscriber
from src.mqtt.mqtt_publisher import publish_scores
from src.ai_models.speech.face_detection import calculate_ear
from src.motor.servo_control import clap_hands
from src.display.touchscreen import display_celebrate
from src.mice_speacker.mice import AudioSegment
#from src.mice_speacker.speacker import 

def main():

    # Start MQTT subscriber
    client = start_mqtt_subscriber()

    # Example session flow
    speak("Hello, what's your name?")
    child_name = recognize_speech()
    speak(f"Nice to meet you, {child_name}")
    
    display_expression("assets/images/happy_face.png")
    set_servo_angle(90, 'arm')  # Move arm to 90 degrees as a greeting
    
    # Simulate a learning session
    session_data = "Sample session data"
    save_session(child_name, session_data)
    
    # Keep the script running to handle incoming MQTT messages
    try:
        while True:
            pass
    except KeyboardInterrupt:
        client.loop_stop()

if __name__ == "__main__":
    main()
