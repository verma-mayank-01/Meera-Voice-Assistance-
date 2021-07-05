import speech_recognition as sr 
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import cv2
import pyautogui
import msvcrt

listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice=listener.listen(source)
            command = listener.recognize_google(voice)
            command=command.lower()
            if 'meera' in command:
                command=command.replace('meera','')

    except:
        pass
    return command
def run_alexa():
    global t
    command=take_command()
    t=0
    print(command)
    if 'i love you' in command:
        talk('i am glad to hear that')
        t=1
    if 'hello' in command:
        talk('hello, how can i help you')
        t=1
    if 'your name' in command:
        talk('my name is meera 1.0')
        t=1
    if 'aapka naam' in command:
        talk('mera naam meera hai')
        t=1
    if 'how are you' in command:
        talk('i am doing great')
        t=1
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
        t=1
    if 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        talk('current time is'+time)
        print(time)
        t=1
    if 'date' in command:
        date=datetime.datetime.now().strftime('%d %B')
        talk('the date is'+date)
        t=1
    if 'day' in command:
        day=datetime.datetime.now().strftime('%A')
        talk('today is '+day)
        t=1
    if 'find about' in command:
        ques=command.replace('find about','')
        info=wikipedia.summary(ques,1)
        talk(info)
        t=1
    if 'meaning' in command:
        mean=command.replace('meaning','')
        info=wikipedia.summary(mean,1)
        talk(info)
        t=1
    if 'your father' in command:
        talk('My father is Mayank Verma')
        t=1
    if 'you single' in command:
        talk('no, i am commited to my work')
        t=1
    if 'search' in command:
        talk('searching on google')
        sea=command.replace('search','')
        pywhatkit.search(sea)
        t=1
    if 'gmail' in command:
        talk('opening mail')
        pywhatkit.search('gmail')
        t=1
    #if 'temperature' in command:
    if 'joke' in command:
        talk(pyjokes.get_joke())
        t=1
    if 'bye'in command:
        talk('see you soon')
        t=2
    if 'no' in command:
        talk('ok good bye')
        t=2
    if 'thank you' in command:
        talk('happy to serve you, any other help?')
        t=1

    if t==0:
        talk('i am not trained that much to do that task')
        talk('i will tell mayank to programme me for your task')
        talk('say other command')
    
run_alexa()
while t!=2:
    run_alexa()

