#to speak any text 

import pyttsx3   

engine = pyttsx3.init()

#setting rate 
rate = engine.getProperty('rate')                    # getting details of current speaking rate
#print (rate)                                        # printing current voice rate
engine.setProperty('rate', 130)                      # setting up new voice rate
 

#setting volume
volume = engine.getProperty('volume')                #getting to know current volume level (min=0 and max=1)
#print (volume)                                      #printing current volume level
engine.setProperty('volume',1.0)                     # setting up volume level  between 0 and 1

#seetting voice
voices = engine.getProperty('voices')                #getting details of current voice
engine.setProperty('voice', voices[0].id)           #changing index, changes voices. o for male
#engine.setProperty('voice', voices[1].id)            #changing index, changes voices. 1 for female

#function to text to voice 
def speak(audio):
    engine.say(audio)                                #use to speech the text 
    print(audio)
    engine.runAndWait()


if __name__ == "__main__":
    speak("vivek")