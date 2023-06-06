#!/usr/bin/python3

import random
import time
import signal

def alarm_handler(signum, frame):
    print('Timeout!')
    exit(1)


def start_menu():
    print('\n')
    print('******************************************')
    print('**         Welcome to our Casino        **')
    print('** Only "Card Sharper" can get the FLAG **')
    print('**       Let\'s join our card game       **')
    print('******************************************')
    print('\n')

if __name__ == "__main__":
    
    signal.signal(signal.SIGALRM, alarm_handler)
    #signal.alarm(60)

    try:
        with open('/flag','r') as f:
            FLAG = f.read()
    except:
        FLAG = 'cce2022{test}'

    start_menu()
    card = [i for i in range(52)]
    sorted_card = [i for i in range(52)]
    seed = input("plz set the seed: ")
    try:
        seed = int(seed)
    except:
        print("seed must be 'int' type")
        exit(-1)
    random.seed(seed)
    round = 1
    while(1):
        print(f"[round {round}] Shuffling the cards...")
        time.sleep(0.5)
        random.shuffle(card)
        if card != sorted_card:
            print('You are not "Card Sharper"!!')
            print('Try harder~')
            exit()
        if round == 50:
            print('\nWOW! you are real "Card Sharper"!!')
            print(f"Here is the FLAG : {FLAG}")
            exit()
        round += 1