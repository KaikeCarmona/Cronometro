import time 
import os

def countdown(t): 
    while t: 
        mins,secs  = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
        dormiu(t)

def dormiu(t):
    if t == 0: 
        os.system("shutdown /s /t 1");


t = input("Insira o tempo em minutos: ") 
countdown(int(t) * 60)