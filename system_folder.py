import os
from speak import speak 
import subprocess 


#fuctions to open system folder 

def open_documents():
    try:
        # os.startfile('C:\\Users\\Vivek Kumar Goel\\Documents')
        subprocess.Popen('explorer "C:\\Users\\Vivek Kumar Goel\\Documents" ')
    except Exception as e :
        speak("No such folder found in the main directory")


def open_downlaods():
    try:
        os.startfile("C:\\Users\\Vivek Kumar Goel\\Downlaods")
    except Exception as e :
        speak("No such folder found in the main directory")


def open_music():
    try:
        os.startfile("C:\\Users\\Vivek Kumar Goel\\Music")
    except Exception as e :
        speak("No such folder found in the main directory")

def open_pictures():
    try:
        os.startfile("C:\\Users\\Vivek Kumar Goel\\Pictures")
    except Exception as e :
        speak("No such folder found in the main directory")

def open_videos():
    try:
        os.startfile("C:\\Users\\Vivek Kumar Goel\\Videos")
    except Exception as e :
        speak("No such folder found in the main directory")

def open_screenshots():
    try:
        os.startfile("C:\\Users\\Vivek Kumar Goel\\Pictures\\Screenshots")
    except Exception as e :
        speak("No such folder found in the main directory")





#function to close system folder 

def close_documents():
    file.terminate()



if __name__ == "__main__":
    open_documents()
    close_documents()
