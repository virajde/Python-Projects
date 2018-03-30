import random

# make a list of words
words = [
    'apple',
    'banana',
    'orange',
    'coconut',
    'strawberry',
    'lime',
    'grapefruit',
    'lemon',
    'kumquat',
    'blueberry',
    'melon'
]  
        
while True:
    start = input("Press enter/return to start, or enter Q to quit ")
    if start.lower() == 'q':
        break
    # pick a random word
    # 'choice' picks the random thing out of an iterabel
    secret_word = random.choice(words)
    bad_guesses = []
    good_guesses = []
    
    while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):
        # draw guessed letters, spaces and strikes
        for letter in secret_word:
            if letter in good_guesses:
                # " end='' " this prints multiple times on the same line
                print(letter, end='') 
            else:
                print('_', end='')
        
        print('')
        print('Strikes: {}/7'.format(len(bad_guesses)))
        print('')
              
        # take guess
        # we are lower-casing it as soon as it comes in
        guess = input("Guess a letter: ").lower()
        
        # Below are the checks needs to be passed after user guess a letter
        # guess is a good guess?
        if len(guess) != 1:
            print("You can only guess a single letter!")
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print("You've already guessed that letter!")
            continue
        # "isalpha()" checks if all the characters are letters in guess
        elif not guess.isalpha():
            print("You can only guess letters!")
            continue
        
        if guess in secret_word:
            good_guesses.append(guess)
            if len(good_guesses) == len(list(secret_word)):
                print("You win! The word was {}".format(secret_word))
                break
        else:
            bad_guesses.append(guess)
    else:
        print("You didn't guess it! My secret word was {}".format(secret_word))  
        
        