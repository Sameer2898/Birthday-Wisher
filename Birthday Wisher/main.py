import os
import random
from Wish.art import *
from time import sleep
from termcolor import colored

input(colored('Press {Enter}.....', 'blue'))
os.system('clear')

for i in range(len(code)):
    print(code[i], sep='', end='', flush=True)
    sleep(.02)

color = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
input(colored('\n{Enter}','red'))
os.system('reset')

def colorful_bars(x, times=135):
    if x == 'open':
        bar = ''
    elif x == 'close':
        bar = ''
    for i in range(times):
        print(colored(bar, random.choice(color)), end='')

#Falling Objects
def fall(lsts, time):
    for i in lsts:
        for j in range(len(i)):
            print(colored(i[j], random.choice(color)), sep='', end='', flush=True);sleep(time)

colorful_bars('open')

#Objects
obj = [cake, man, book]
fall(obj, 0.005)
colorful_bars('close')

input()
os.system('reset')

#Face in ASCII 
print('Change the background color to white and font color to black')
input('Enter the command {cntrl+ -} four times and press {enter}.....' )

for i in range(len(face)):
    print(face[i], sep='', end='', flush=True);sleep(0.002)