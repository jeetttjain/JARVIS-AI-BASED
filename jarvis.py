import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import wikipedia
import webbrowser
import pywhatkit
import os
import sys

engine.setPengine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
roperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("good morning sir!")

    elif 12 <= hour < 18:
        speak("good afternoon sir!")

    else:
        speak("good evening sir!")

    speak("i am jarvis. please tell me how may i help you.")


def takecommand():
    # it
    listener = Recognizer()
    with Microphone() as source:
        print("listening...")
        voice = listener.listen(source)
        listener.recognize_google(voice)
        listener.pause_threshold = 1
        audio = listener.listen(source)
    try:

        print("recognizing...")
        listener.recognize_google(audio, language="en-in")
        print(f"user said: {query}\n ")

    except exception as e:

        print("say that again please...")
        speak(" sir,say that again please...")
        return "none"
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        # logic
        if 'search' in query:
            speak('searching ...')
            query = query.replace('search', '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to google")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'play' in query:
            song = query.replace('play', '')
            speak('okay,enjoy your music!' + song)
            pywhatkit.playonyt(song)


        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play my favorite song' in query:
            music_dir = 'D:\\sandisk\\Song\Songs\\'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[22]))

        elif ' the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(F"sir, the time is {strTime}")

        elif 'open code' in query:
            codepath = 'C:\\Users\\Jeet\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codepath)

        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day. ")
            sys.exit()
        speak("sir, do have any other work")
