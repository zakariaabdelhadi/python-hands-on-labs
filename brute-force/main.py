import string
import itertools
import time
from itertools import cycle


def main():
    user_password = input('please enter a password: ')
    startTime = time.perf_counter()

    if brut_forced_passwd := brutForce(user_password):
        print(brut_forced_passwd)

    endTime = time.perf_counter()
    print(f'Time taken for the brut force is {endTime - startTime} ')

def print_searching(dots):
            print(f'\rSearching{dots}   ', end='', flush=True)  # \r = in-place, flush=True = sofortige Ausgabe             

def brutForce(passwd):
    
    passwd_lenght = len(passwd)
    charsPool = string.ascii_letters + string.digits # angenommen besteht nur aus digits und letters
    
    versuch = 0
    found = False
    dots = cycle(['.', '..', '...'])  # zyklischer Generator
    guesses = itertools.product(charsPool, repeat= passwd_lenght)
    for guess in guesses:
        print_searching(dots=next(dots))
        versuch += 1
        if ''.join(guess) == passwd:
           found = True
           return f'\nfound {''.join(guess)} after {versuch} Versuche'



main()


