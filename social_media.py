from speak import speak
import os
import webbrowser

#setting chrome path 
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'


#function to open  program ......

def open_whatsaap():
    speak("Opening Whatsaap")
    try:    
        npath = "C:\\Users\\Vivek Kumar Goel\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
        os.startfile(npath)
    except Exception as e:
        speak('Sorry not able to find whatsaap in main directory ')


def open_instagram():
    speak('Opening Instagram')
    webbrowser.get(chrome_path).open("https://www.instagram.com/")


def open_facebook():
    speak('Opening Facebook')
    webbrowser.get(chrome_path).open("https://www.facebook.com")


def open_stackoverflow():
    speak('Opening StackOverFlow')
    webbrowser.get(chrome_path).open("https://www.stackoverflow.com")

def open_gmail():
    speak('Opening Gmail')
    webbrowser.get(chrome_path).open("https://www.www.gmail.com")




#function to close program ......


def close_whatsaap():
    speak("Closing whatsaap")
    try:
        os.system('TASKKILL /F /IM WhatsApp.exe')
    except Exception as e :
        speak(" whatsaap is not open")



if __name__ == '__main__':
    open_instagram()