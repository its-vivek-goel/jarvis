from pydub import AudioSegment 
from pydub.playback import play 

def notification_sound():
    song = AudioSegment.from_wav("chime.wav")
    play(song)
