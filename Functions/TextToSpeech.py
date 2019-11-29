import pyttsx3
def Text2Speech(text):
	engine = pyttsx3.init()
	engine.say(text)
	engine.setProperty('rate',120)
	engine.setProperty('volume', 2.0)
	engine.runAndWait()
	Text2Speech(text)