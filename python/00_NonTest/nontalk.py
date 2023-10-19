import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Capture audio from your microphone
with sr.Microphone() as source:
    print("Say something:")
    audio = recognizer.listen(source)

# Recognize the speech using Google Web Speech API
try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Could not understand the audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Web Speech API; {e}")

# Alternatively, you can use other speech recognition engines like CMU Sphinx:
# try:
#     text = recognizer.recognize_sphinx(audio)
#     print("You said:", text)
# except sr.UnknownValueError:
#     print("Could not understand the audio")
# except sr.RequestError as e:
#     print(f"Recognition request failed; {e}")
