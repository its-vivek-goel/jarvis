#main function to excute task

import pyttsx3                                       # use to convert text to voice 
import speech_recognition as sr                      # use to convert voice to machine readable language
import datetime
import os
import wikipedia
import webbrowser
import cv2
import random 

from requests import get                             # to get ip address
import pywhatkit                                     # to send message using whatsapp
import sys 
import pyautogui
import time 


#self made class 

from speak import speak 
from takecommand import takecommand
from jarvis_status import jarvis_status
from wish import wish 


#setting chrome path 
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

def task_execution():
    # wish()

    query = takecommand()                                 #taking query from user 

    #logic for task begin 

    if 'wikipedia' in query:
        speak("Searching in Wikipedia , Please wait ... ")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query , sentences=2)
        speak("According to Wikipedia")
        speak(results)

    #basic conversation 

    elif 'hello' in query:
        speak('Namaste sir')

    elif 'how are you' in query:
        speak('I am fine sir, what about you ?')

    elif 'i am also good' in query or 'i am good' in query:
        speak("That's great to hear from you")

    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)
        speak(f"Sir , time is {strTime}")


        #to open system app 

    elif 'open notepad' in query :
        speak("Opening Notepad")
        npath = 'C:\\Windows\\system32\\notepad.exe'
        os.startfile(npath)


    elif 'open chrome' in query or 'open google chrome' in query :
        speak("Opening Google Chrome")
        cpath = '"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"'
        os.startfile(cpath)

    elif 'open cmd' in query or 'open command prompt' in query  :
        speak("Opening cmd")
        os.system('start cmd')

    elif 'open calculator' in query :
        speak("Opening Calculator")
        cal_path = 'C:\\Windows\\System32\\calc.exe'
        os.startfile(cal_path)

        #to close system app

    elif 'close notepad' in query :
        speak("Closing Notepad")
        os.system('TASKKILL /F /IM notepad.exe')

    elif 'close chrome' in query or 'close google' in query:
        speak("Closing Chrome")
        os.system('TASKKILL /F /IM chrome.exe')

    elif 'close cmd' in query :
        speak("Closing Cmd")
        os.system('TASKKILL /F /IM cmd.exe')
        

    elif 'close calculator' in query :
        speak("Closing Calculator")
        os.system('TASKKILL /F /IM calc.exe')
        

        #to open camera

        # elif "open camera" in query :
        #     cap = cv2.VideoCapture(0)                   # 0 -> indicate we are using internal camera 
        #     while True:
        #         ret , img = cap.read()
        #         cv2.imshow('webcam' , img)
        #         k = cv2.waitKey(50)
        #         if k==27:
        #             break
        #     cap.release()
        #     cv2.destroyAllWindows() 

        # to play music

    elif 'play music' in query :
        music_dir = "E:\\songs"
        songs = os.listdir(music_dir)
        song_list = []
        for song in songs :
            if song.endswith('.mp3'):              #if folder contain more file slecting only song
                song_list.append(song)
            
        if len(song_list)>0:
            song_rd = random.choice(song_list)
            os.startfile(os.path.join(music_dir,song_rd))
        else:
            speak("No song found in the directory ")

        #to get ip

    elif 'ip address' in query:
        ip = get('https://api.ipify.org').text
        speak(f'your IP address is {ip}')

        #to get location 

    elif 'where i am' in query or 'where we are' in query or 'find my location' in query :
        speak("Wait sir , let me check your location")

        try :
            ipAdd = get('https://api.ipify.org').text
            print(ipAdd)
            url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
            geo_requests = get(url)
            geo_data = geo_requests.json()
            city = geo_data['city']
            country = geo_data['country']
            speak(f"Sir I am not sure , but i think we are in {city} city of {country} country")

        except Exception as e:
            speak("Sorry sir , due to network issue i am not able to find where we are")
        #to take screenshot

    elif 'take screenshot' in query or 'take a screenshot' in query :
        speak('Sir , please tell me the name for this screenshot file')
        name = takecommand()
        speak('Please sir hold the screen for few seconds , i am taking screenshot')
        time.sleep(2)
        img = pyautogui.screenshot()
        img.save(f'{name}.png')
        speak('I am done sir , the screenshoot is saved in our main folder .')


        # opening different sites 


    elif 'open google' in query:
        speak('Opening Google')
        webbrowser.get(chrome_path).open("google.com")

    elif 'open youtube' in query:
        speak('Opening Youtube')
        webbrowser.get(chrome_path).open("youtube.com")       #chrome_path used to open chrome we have set dirc above  

    elif 'play song on youtube' in query or 'play songs on youtube' in query:
        speak('which song do you want to play')
        cm = takecommand()
        speak(f'playing {cm} on youtube')
        pywhatkit.playonyt(f'{cm}')

    elif 'open gmail' in query:
        speak('Opening Gmail')
        webbrowser.get(chrome_path).open("www.gmail.com")


    elif 'open facebook' in query:
        speak('Opening Facebook')
        webbrowser.get(chrome_path).open("facebook.com")

    elif 'open whatsaap' in query:
        speak('Opening Whatsaap')
        webbrowser.get(chrome_path).open("https://web.whatsapp.com/")

    elif 'open instagram' in query:
        speak('Opening Instagram')
        webbrowser.get(chrome_path).open("https://www.instagram.com/")

    elif 'open stack overflow' in query:
        speak('Opening StackOverFlow')
        webbrowser.get(chrome_path).open("stackoverflow.com")

        #to perform opertaion with system 
    elif 'switch the window' in query :
        pyautogui.keyDown('alt')
        pyautogui.press("tab")
        pyautogui.keyUp('alt')


        #to close the program
    elif 'sleep' in query or 'no thanks' in query :
        speak('okay sir , i am going to sleep you can call me anytime')
        # break

        #when no data match 
    elif 'none' in query or '' in query:
        speak("I didn't get you say that again please...")