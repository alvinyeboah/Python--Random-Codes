import speech_recognition as sr

# Create a recognizer object
recognizer = sr.Recognizer()

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Say something...")
    audio = recognizer.listen(source)

try:
    # Recognize the speech
    text = recognizer.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Could not understand the audio.")
except sr.RequestError as e:
    print(f"Error: {e}")
