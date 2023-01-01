import pyttsx3
import datetime
import speech_recognition as sr

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(talk):
    engine.say(talk)
    engine.runAndWait()


def wish():
    q=int(datetime.datetime.now().hour)
    if(q<12):
        speak('Good Morning')
    elif(q>12 or q<18):
        speak('Good Afternoon')
    else:
        speak('Good evening')

def command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print('Recognizing')
        query=r.recognize_sphinx(audio,language='en-in')
        print(query)

    except Exception as e:
        print(e)
        return 'None'
    
    # return query






wish()
# speak('I am Talha')
command()