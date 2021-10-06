#function to wish 

import datetime
from speak import speak

def wish():

    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    hour = int(now.hour)

    if hour>=0 and hour<12:
        speak(f'good morning sir , its {current_time}')

    elif hour>=12 and hour<18 :
        speak(f'good afternoon sir , its {current_time}')

    else:
        speak(f'good evening sir , its {current_time}')

    speak('I am Jarvis . Please tell me how may i help you ??')


if __name__ == '__main__':
    wish()