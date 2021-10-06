#this file contain work like tell date , time , joke , weather

import datetime 
import requests
from bs4 import BeautifulSoup
from speak import speak 
from takecommand import takecommand
from urllib.request import urlopen
import pyjokes


def speak_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    speak(f"It's {current_time}")


def speak_date():
    now = datetime.datetime.now()
    current_date = now.strftime("%B %d %Y")
    speak(f"Today is {current_date}")


def speak_temperature():
    speak("Which city temperature do you want to know ?")
    city = takecommand()
    weather = f"temperature in {city}"
    url = f"https://www.google.com/search?q={weather}"
    r = requests.get(url)
    data = BeautifulSoup(r.text , "html.parser")
    temp = data.find("div", class_ ="BNeawe").text
    speak(f"Current temperature in {city} is {temp}")



def speak_news():
    speak("Please hold on searching top headlines")
    news_url = "https://news.google.com/news/rss"
    Client = urlopen(news_url)
    xml_page = Client.read()
    Client.close()
    soup_page = BeautifulSoup(xml_page , "xml")
    news_list = soup_page.find_all("item" , limit = 5)

    speak("today's headlines")
    i = 1
    for news in news_list:
        speak(f"{i}. {news.title.text}")
        i = i+1


def speak_joke():
    status = 'yes'
    while True:
        if 'yes' in status:
            my_jokes  = pyjokes.get_joke()
            speak(my_jokes)
            speak("Do you want to listen more")
            status = takecommand()
        else:
            break




if __name__ == '__main__':
    # speak_time()
    # speak_date()
    # speak_temperature()
    # speak_news()
    speak_joke()

    
