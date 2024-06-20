import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")

        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)

        # Capture the audio
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")

        # Use Google Web Speech API to recognize the audio
        text = recognizer.recognize_google(audio)

        # Print recognized text
        print(f"You said: {text}")

    except sr.UnknownValueError:
        print("Sorry, could not understand what you said.")

    except sr.RequestError as e:
        print(f"Request error from Google Speech Recognition service: {e}")

# Call the speech recognition function
recognize_speech()
