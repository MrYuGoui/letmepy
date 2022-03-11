import winsound
from playsound import playsound
import win32com.client
import pyttsx3
from time import sleep,ctime
import threading,multiprocessing

def PAL():
    playsound('PPP.mp3')

def YinJie():
    # winsound.Beep(523,1000)   1
    # winsound.Beep(587,1000)   2
    # winsound.Beep(659,1000)   3
    # winsound.Beep(698,1000)   4
    # winsound.Beep(784,1000)   5
    # winsound.Beep(880,1000)   6
    # winsound.Beep(988,1000)   7
    # winsound.Beep(1046,1000)  1+
    # winsound.Beep(1175,1000)  2+
    # winsound.Beep(1318,1000)  3+
    # winsound.Beep(1397,1000)  4+
    # winsound.Beep(1568,1000)  5+
    winsound.Beep(1318,200)
    winsound.Beep(1175,200)
    winsound.Beep(1318,200)
    winsound.Beep(1175,200)
    winsound.Beep(1318,200)
    winsound.Beep(988,200)
    winsound.Beep(1175,200)
    winsound.Beep(1046,200)
    winsound.Beep(880,200)

def Speak_test1():
    speaker=win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak("fucking asshole,你这皮皮猪")

def Speak_test2():
    engine=pyttsx3.init()
    voices = engine.getProperty('voices')
    # for voice in voices:
    #     engine.setProperty('voice', voice.id)
    #     engine.say('你好呀')
    # engine.say("fucking asshole")
    # rate = engine.getProperty('rate')
    # engine.setProperty('rate', rate + 50)

    engine.say('the lazy dog.')
    engine.say("你这皮皮猪")
    engine.runAndWait()

# threads=[]
# t1=threading.Thread(target=YinJie)
# threads.append(t1)
# t2=threading.Thread(target=PAL)
# threads.append(t2)

if __name__ == "__main__":
    # for t in threads:
    #     t.start()
    # for t in threads:
    #     t.join()