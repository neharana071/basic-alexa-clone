import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



engine.say('Hi, I am Alexa')
engine.say('What can I do for you?')
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()
while True:
    def take_command():
        try:
            with sr.Microphone() as source:
                print('Listening...')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'alexa' in command:
                    command = command.replace('alexa', '')
                    print(command)
        except:
            pass
        return command

    def alexa_run():
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('Playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk('The current time is ' + time)
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'made' in command:
            talk('I was made by my beautiful developer, Neha Rana')
        elif 'old' in command:
            talk('I was just developed today')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        else:
            talk('Please say that again')






