import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("good morning sir")
    
    elif hour>12  and hour<18:
        speak("good afternoon sir")
    
    else :
        speak("good evening sir")

    


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.
        

    except Exception as e:
        print(e)    
        speak("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query
    


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'from wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            speak(results)
        
        elif 'open youtube' in query:
            speak("opening youtube sir")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("opening google sir")
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S:%p")
            speak(f"sir , the time is {strTime}")
        
        elif 'open code' in query:
            speak("opening code sir")
            codePath ="C:\\Users\\asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)


        elif 'open snake game' in query:
            speak("opening sir")
            path ="D:\\python practice\\snake game\\dist\\game.exe"
            os.startfile(path)
        
        elif 'hello'in query:
            speak("hello sir , tell me what can I do for you")

        elif 'goodbye'in query:
            speak("good bye sir , and have a great day")
        False

                


        