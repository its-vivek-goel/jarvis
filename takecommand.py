#to take command from user in audio and  convert it into text 

import speech_recognition as sr                      # use to convert voice to machine readable language

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source ,timeout = 10 , phrase_time_limit = 5)

        try :
            print("Recognizing...")
            query = r.recognize_google(audio , language = 'en-in')
            query = query.lower()                     #to convert all the text in lower character
            print(f'User said : {query}')

        except Exception as e :                        
            return "none"

        return query 


if __name__ == "__main__":
    data = takecommand()
    print(data)