from pygame import mixer
import datetime
from time import time

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylog.txt","a") as f:
        f.write(f"{msg} {datetime.datetime.now()}")

if __name__ == '__main__':
    # musiconloop("water.mp3","stop")
    init_water = time()
    init_eyes = time()
    init_exe = time()
    watersecs = 5
    eyessecs =  10
    exe = 15

while True:
    if time() - init_water > watersecs:
        print("water drinking time. Enter 'drank' to stop the alarm.")
        musiconloop('water.mp3','drank')
        init_water = time()
        log_now("Drank water at")

    if time() - init_eyes > eyessecs:
        print("Eye Exercise time. Enter 'done' to stop the alarm.")
        # musiconloop('water.mp3','drank')
        init_eyes = time()
        log_now("Physical activity at")

    if time() - init_exe > exe :
        print("Eye Exercise time. Enter 'done' to stop the alarm.")
        # musiconloop('water.mp3','drank')
        init_exe = time()
        log_now("Physical activity at")