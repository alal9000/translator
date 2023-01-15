import speech_recognition as sr
import pyttsx3
from translate import Translator


# Initialize the recognizer
r = sr.Recognizer()

# Start listening to the microphone
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# Recognize the speech
try:
    text = r.recognize_google(audio)
    print("You said: {}".format(text))
except sr.UnknownValueError:
    print("Sorry, I could not understand what you said.")
except sr.RequestError as e:
    print("Error: {}".format(e))

translator = Translator(to_lang="es")
translation = translator.translate(text)
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say(text)
print(translation)
engine.say(translation)
engine.runAndWait()
