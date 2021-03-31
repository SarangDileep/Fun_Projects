import speech_recognition as fun
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import random

def talk(*text):
    jarvis.say(text)
    jarvis.runAndWait()

listener=fun.Recognizer()
jarvis=pyttsx3.init()
jarvis.setProperty('rate', 120) 
voices=jarvis.getProperty('voices')
jarvis.setProperty("voice",voices[22].id)
intro1="Hi I am jarvis"
intro2="How can I help you"
talk(intro1,intro2)
while(1):
    try:
        with fun.Microphone() as src:
            print("Listening....")
            voice=listener.listen(src)
            command=listener.recognize_google(voice)
            command=command.lower()
            print(command)
            if("jarvis" in command):
                if("play" in command):
                    search_text=command[command.index("play")+len("play"):]
                    talk("playing",search_text)
                    pywhatkit.playonyt(search_text)
                elif("time" in command):
                    current_time=datetime.datetime.now().strftime("%I:%M %p")
                    talk("Time is",current_time)
                elif("wiki" in command):
                    search_text=command[command.index("wiki")+len("wiki"):]
                    result=wikipedia.summary(search_text,1)
                    print(result)
                    talk(result)
                elif("joke" in command):
                    talk(pyjokes.get_joke())
                elif("toss" in command):
                    coin=["tail","head"]
                    talk("It is",random.choice(coin))
                elif("die" in command):
                    die=[1,2,3,4,5,6]
                    talk("It is",random.choice(die))
                else:
                    talk("sorry","come again")
    except:
        pass
