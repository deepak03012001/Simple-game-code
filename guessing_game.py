import random

def guessnum():
    guess=0
    numrange=int(input('Enter number to decide range for picking the magic number..'))
    num=random.randint(0,numrange)
    while True:
        guess+=1
        print(f"Guessing for {guess}th time...")
        guess_num=input()
        if int(guess_num)==num:
            print(f"guessed it right, the answer is-{guess_num} and you took {guess} attempts!!!")
            quit()
        else:
            print('try again..')


guessnum()