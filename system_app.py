from speak import speak
import os


def open_notepad():
    speak("Opening Notepad")
    try:    
        npath = 'C:\\Windows\\system32\\notepad.exe'
        os.startfile(npath)
    except Exception as e:
        speak('Sorry not able to find notepad on main directory')


def open_calculator():
    speak("Opening Calculator")
    try:
        cal_path = 'C:\\Windows\\System32\\calc.exe'
        os.startfile(cal_path)
    except Exception as e :
        speak('Sorry not able to find calculator in main directory ')



def open_cmd():
    speak("Opening Cmd")
    try:    
        npath = 'C:\\Users\\Vivek Kumar Goel\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt'
        os.startfile(npath)
    except Exception as e:
        speak('Sorry not able to find cmd in main directory ')



def open_control_panel():
    speak("Opening Control Panel")
    try:    
        npath = 'C:\\Users\\Vivek Kumar Goel\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel'
        os.startfile(npath)
    except Exception as e:
        speak('Sorry not able to find cmd in main directory ')



def open_chrome():
    speak("Opening Google Chrome")
    try:
        cpath = '"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"'
        os.startfile(cpath)
    except Exception as e:
        speak('Sorry not able to find chrome in main directory ')

#closing file 

def close_notepad():
    speak("Closing Notepad")
    try:
        os.system('TASKKILL /F /IM notepad.exe')
    except Exception as e :
        speak(" Notepad is not open")


def close_calculator():
    speak("Closing calculator")
    try:
        os.system('TASKKILL /F /IM calculator.exe')
    except Exception as e :
        speak(" calculator is not open")


def close_cmd():
    speak("Closing Cmd")
    try:
        os.system('TASKKILL /F /IM cmd.exe')
    except Exception as e :
        speak(" Cmd is not open")


def close_control_panel():
    speak("Closing Control Panel")
    try:
        os.system('TASKKILL /F /IM control.exe')
    except Exception as e :
        speak(" Control Panel is not open")


def close_chrome():
    speak("Closing chrome")
    try:
        os.system('TASKKILL /F /IM chrome.exe')
    except Exception as e :
        speak(" chrome is not open")

