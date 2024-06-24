import azure.cognitiveservices.speech as speechsdk
from pydub import AudioSegment
import pyaudio
import wave

# Azure Speech Service credentials
SPEECH_KEY = "YOUR_SPEECH_KEY"
SPEECH_REGION = "YOUR_SPEECH_REGION"

# Function to record audio from the microphone
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

    for _ in range(0, int(RATE / CHUNK * duration)):
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

# Function to recognize speech and assess pronunciation from an audio file
def recognize_from_audio(label, audio_file):
    speech_config = speechsdk.SpeechConfig(
        subscription=SPEECH_KEY, region=SPEECH_REGION
    )
    speech_config.set_property(speechsdk.PropertyId.Speech_LogFilename, "speechsdk.log")
    speech_config.speech_recognition_language = "ar-SA"

    audio_config = speechsdk.audio.AudioConfig(filename=audio_file)

    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config, audio_config=audio_config
    )

    pronunciation_assessment_config = speechsdk.PronunciationAssessmentConfig(
        json_string=f'{{"ReferenceText":"{label}","gradingSystem":"HundredMark","granularity":"Word"}}'
    )

    pronunciation_assessment_config.apply_to(speech_recognizer)

    speech_recognition_result = speech_recognizer.recognize_once()

    pronunciation_assessment_result = speechsdk.PronunciationAssessmentResult(speech_recognition_result)

    return pronunciation_assessment_result

# Function to convert any audio file to WAV format (if needed)
def convert_to_wav(audio_file, audio_file_path):
    with open(audio_file_path, "wb") as f:
        f.write(audio_file)
        f.close()

    sound = AudioSegment.from_file(audio_file_path)
    sound.export(audio_file_path, format="wav")

    return audio_file_path

# Function to predict the pronunciation score
def predict_score(label, audio_file_path):
    result = recognize_from_audio(label, audio_file_path)

    if result.accuracy_score >= 50:
        return "passed", result.accuracy_score
    else:
        return "failed", result.accuracy_score

# Main function to record audio, recognize speech, and assess pronunciation
def assess_pronunciation(label, audio_file_path='recorded_audio.wav', duration=5):
    # Record audio
    record_audio(audio_file_path, duration)

    # Predict the pronunciation score
    result = predict_score(label, audio_file_path)
    return result
