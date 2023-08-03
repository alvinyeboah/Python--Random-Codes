import speech_recognition as sr



def transcribe_audio(audio_file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.record(source)

        try:
            transcribed_text = recognizer.recognize_google(audio_data)
            return transcribed_text
        except sr.UnknownValueError:
            print("Speech Recognition could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    audio_file_path = '/Users/alvinyeboah/Downloads/1_Introduction to Thesis Statements/21_1_Introduction to Thesis Statements.wav'
    
    transcribed_text = transcribe_audio(audio_file_path)
    if transcribed_text:
        print("Transcription:")
        print(transcribed_text)
