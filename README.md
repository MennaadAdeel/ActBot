
# ***Humanoid Robot for Autism Communication Aid (ActBot)***


This project aims to develop a humanoid robot designed to assist children with autism in improving their communication skills. The robot interacts with the child using a combination of speech recognition, text-to-speech, servo motor movements, and visual displays on a touchscreen. The entire system is controlled by a Raspberry Pi and communicates with a mobile application using the MQTT protocol. The robot provides engaging and interactive sessions to help children practice and enhance their communication abilities in a friendly and supportive environment.



# **Features**

- **Personalized Interaction:** The robot welcomes the child by name and engages them in interactive sessions.
- **Speech Recognition:** Uses state-of-the-art speech recognition technology to understand and respond to the child’s spoken words.
- **Text-to-Speech:** Communicates with the child using natural-sounding speech synthesis.
- **Facial Expressions:** Displays various facial expressions on a touchscreen to enhance interaction and provide visual feedback.
- **Motor Movements:** Uses servo motors to move the robot’s arms and neck, adding a physical dimension to the interaction.
- **Session Feedback:** Tracks the child’s progress and sends feedback and scores to a mobile application, which suggests further activities based on performance.
- **MQTT Communication:** Ensures seamless communication between the robot and the mobile app for real-time updates and control.



# **Components**

( **Hardware** )

  - Raspberry Pi: The main controller for the robot.
  - Raspberry Pi Camera: Captures images and videos for interaction.
- Servo Motors: Control the movements of the robot’s arms and neck.
- Touchscreen Display: Shows facial expressions and session progress.
- Speakers and Microphone: Facilitates audio interaction with the child.


( **Software** )
 
 - Speech Recognition: Implements accurate speech-to-text conversion.
 - Text-to-Speech: Provides engaging and clear spoken feedback.
- MQTT Protocol: Manages communication between the robot and the mobile app.
- Database: Stores session data and tracks progress over time.
- Python: The main programming language used for developing the robot’s functionalities.


# **Getting Started**

**Prerequisites**
- Raspberry Pi with Raspbian OS installed.
- Python 3.x.
- Various Python libraries: paho-mqtt, speech_recognition, pyttsx3, RPi.GPIO, pygame, picamera, etc.



# **Installation**

**1. Clone the repository:**

 -      git clone https://github.com/MennaadAdeel/ActBot.git
 -      cd ActBot
**2.Install the required Python libraries:**

-       pip3 install -r requirements.txt


# **Configuration**

- Configure MQTT broker details in config/config.py.
- Set up the database by running the initialization script.


# **Running the Project**

- Power on the Raspberry Pi and connect all hardware components.

- Run the main script:

       python3 src/main.py*


# **Usage**

- Power On: Turn on the robot and it will welcome the child by name.
- Interactive Session: The robot will conduct a session where the child repeats phrases and interacts with the robot.
- Feedback: After the session, feedback and scores are sent to the mobile app for further activity suggestions.
- Continuous Learning: The robot tracks progress over multiple sessions to adapt and personalize the learning experience.


# **Contributing**

We welcome contributions to improve the project. Please fork the repository and create a pull request with your changes.

# **License**
This project is licensed under the MIT License - see the LICENSE file for details.


# **Acknowledgments**

- Inspiration from projects like Lux AI robot.
- Open-source libraries and tools that made this project possible.



  

