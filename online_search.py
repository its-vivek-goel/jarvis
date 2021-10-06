#this file is use to search online content on chrome , translate sentence , word meaning , so on 

from takecommand import takecommand
from speak import speak 
import webbrowser
import wikipedia
from google_trans_new import google_translator

#setting chrome path 
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

def search_on_chrome():
    speak("What should I search on Chrome, sir")
    search = takecommand()
    search = search.replace(" " , "")                   #use to repalce space taken from user in command
    if search == 'none':
        speak("Sorry i didn't get you ")
    else:
        webbrowser.get(chrome_path).open_new_tab('www.'+search+'.com')
    
def search_in_wikipedia(query):
    speak("Searching in Wikipedia , Please wait ... ")
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query , sentences=2)
    speak("According to Wikipedia")
    speak(results)


def translate_sentence(query):
    translator = google_translator()  
    query = query 
    translate_text = translator.translate(query ,lang_src='en' ,lang_tgt='hi')  
    prinT(translate_text)     #how to speak this hindi text 



if __name__ == '__main__':
    # search_on_chrome()
    # search_in_wikipedia("python")
    translate_sentence('how are you')

