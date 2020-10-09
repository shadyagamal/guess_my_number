# -*- coding: utf-8 -*-

'''
this script will try to guess the mysterious number
prepared by guess_my_number.GuessMachine.
It's strategy is to try random numbers.
'''

import random
from guess_my_number import MIN, MAX, GuessMachine

if __name__=='__main__':
    guess_machine=GuessMachine()
    while True:
        attempt= random.randint(MIN,MAX)
        result= guess_machine.guess(attempt)
        print('tried %d : %s' % (attempt, result))
        if result == 'found':
            print('Finished in %d attempts.' % guess_machine.number_of_attempt)
            break
