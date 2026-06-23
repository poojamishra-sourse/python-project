import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import time

def sptext(): #sune ke liye
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
    try:
        print("Recognizing...")
        data=recognizer.recognize_google(audio)
        print(data)
        return data
    except:
        print("Not recognized")
        return None

def speechtx(x): #bolne ke liye
    ENGINE=pyttsx3.init()
    voice=ENGINE.getProperty('voices')
    ENGINE.setProperty('voice',voice[1].id)
    ENGINE.setProperty('rate',150)
    ENGINE.say(x)
    ENGINE.runAndWait()

if __name__=="__main__":

    command = sptext()
    if command and "hey google" in command.lower():

        while True:
            data1 = sptext()
            if not data1:
                continue
            data1 = data1.lower()

            if "your name" in data1:
                speechtx("my name is google")
            elif "old are you" in data1:
                speechtx("i am twelve years old")
            elif "time" in data1:
                time_now=datetime.datetime.now().strftime("%I:%M %p")
                speechtx(time_now)
            elif "youtube" in data1:
                webbrowser.open("https://www.youtube.com/")
            elif "web" in data1:
                webbrowser.open("https://www.google.com/")
            elif "joke" in data1:
                joke_1=pyjokes.get_joke()
                print(joke_1)
                speechtx(joke_1)
            elif "play song" in data1:
                webbrowser.open("https://www.youtube.com/watch?v=H78YW7ycuwI&list=RDH78YW7ycuwI&start_radio=1")
            elif "exit" in data1:
                speechtx("thank you for using me have a nice day")
                break

            time.sleep(2)

      
                 
          


    
