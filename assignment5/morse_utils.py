# Wrapper round time and winsound functions required for automarker.
import time
import winsound

def sleep(duration):
    time.sleep(duration)
    
def beep(frequency, duration):
    winsound.Beep(frequency, duration)