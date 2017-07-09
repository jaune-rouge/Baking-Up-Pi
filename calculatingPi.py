# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 16:35:50 2017

@author: J
"""

#%%
res = 4
print("We'll try to calculate pi. Starting at 4 and getting closer and closer.\n")
print(" THE GAME ".center(80,'*'))
while True:
    try:
        numGuesses = int(input("How many round of guessing would you like to do? "))
        break
    except ValueError:
        print("Please provide a number.")
print("Guess #1: "+str(res))

oddNum = 3
for guess in range(2,numGuesses+1):
    sq = oddNum**2
    res = res * (sq-1)/sq
    oddNum += 2
    print("Guess #"+str(guess)+": "+str(res))
exit()

