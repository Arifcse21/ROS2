import pyttsx3

tts = pyttsx3.init()

val = "hello"

tts.say(val)
tts.runAndWait()
