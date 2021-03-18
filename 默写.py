import pyttsx3

engine = pyttsx3.init()
for line in open("./abc.txt"):
    print(line)
    engine.say(line)
    engine.runAndWait()
