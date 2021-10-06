
#main function to perform jarvis (this operation will be performed once jarvis called )

from task_execution import task_execution

from notification_sound import notification_sound

from jarvis_status import jarvis_status
from speak import speak
import time 
import sys 
from wish import wish




def jarvis():

    wish()
    while True:
        permission = jarvis_status()

        if "jarvis" in permission or "hey jarvis" in permission:
            notification_sound()
            task_execution()
