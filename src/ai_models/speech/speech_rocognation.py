import azure.cognitiveservices.speech as speechsdk
from pydub import AudioSegment
import pyaudio
import wave

def record_audio(audio_file_path, duration=5):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    frames = []

    print("Recording...")

    for i in range(0, int(RATE / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(audio_file_path, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

def recognize_from_audio(label, audio_file):
    SPEECH_KEY = "5e8fed82a65f498aa2c5516947e762a4"
    SPEECH_REGION = "eastus"
    speech_config = speechsdk.SpeechConfig(
        subscription=SPEECH_KEY, region=SPEECH_REGION
    )
    speech_config.set_property(speechsdk.PropertyId.Speech_LogFilename, "speechsdk.log")

    speech_config.speech_recognition_language = "ar-SA"

    audio_config = speechsdk.audio.AudioConfig(filename=audio_file)

    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config, audio_config=audio_config
    )

    pronunciation_assessment_config = speechsdk.PronunciationAssessmentConfig(json_string="{{\"ReferenceText\":\"{}\",\"gradingSystem\":\"HundredMark\",\"granularity\":\"Word\"}}".format(label))

    pronunciation_assessment_config.apply_to(speech_recognizer)

    speech_recognition_result = speech_recognizer.recognize_once()

    pronunciation_assessment_result = speechsdk.PronunciationAssessmentResult(speech_recognition_result)

    return pronunciation_assessment_result

def convert_to_wav(audio_file, audio_file_path):
    with open(audio_file_path, "wb") as f:
        f.write(audio_file)
        f.close()

        sound = AudioSegment.from_file(audio_file_path)
        sound.export(audio_file_path, format="wav") 

    return audio_file_path

def predict_score(label, audio_file_path):
    result = recognize_from_audio(label, audio_file_path)
    
    if result._accuracy_score >= 50:
        return ("passed", result._accuracy_score)
    else:
        return ("failed", result._accuracy_score)
    
    
    # Replace 'تفاحة' with the desired label for pronunciation assessment
label = 'تفاحة'
audio_file_path = 'recorded_audio.wav'

# Record audio from the microphone
record_audio(audio_file_path)

# Predict the pronunciation score
result = predict_score(label, audio_file_path)
print(result)