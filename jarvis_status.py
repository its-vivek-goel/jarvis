#function to add wakeup command 

import speech_recognition as sr

def jarvis_status():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.adjust_for_ambient_noise(source)
        print("Jarvis is sleeping ..")
        r.pause_threshold = 1
        audio = r.listen(source ,timeout = 20 , phrase_time_limit = 15)

        try :
            # print("Recognizing...")
            query = r.recognize_google(audio , language = 'en-in')
            query = query.lower()                     #to convert all the text in lower character

        except Exception as e :                        
            return "none"

        return query 

if __name__ == "__main__":
    query = jarvis_status()
    print(query)