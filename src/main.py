import mqtt
import ai_models
import motor
import display
import mice_speacker

def main():
    # Initialize components
    initialize_database()

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
