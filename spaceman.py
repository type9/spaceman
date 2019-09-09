import random
# GLOBALS
guessed_word_joinchar = ""  # "" for nothing between the characters e.g. "_AT"
# DEBUGGING GLOBALS
DEBUG = True
TESTMODE = False
TESTWORD = "CAT"
TESTGUESSES = "C_T"
TESTGUESS = "A"
TESTLETTERSGUESSED = "AT"


def load_word():
    """
    A function that reads a text file of words and randomly selects one to use
    as the secret word
        from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game
    """
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word, letters_guessed):
    """
    A function that checks if all the letters of the secret word have been
    guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been
        guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in
        letters_guessed, False otherwise
    """
    # loops through both words to see if each letter is the same.
    # if all indexes are the same the output is true.
    # if any index is different it stops the loop by returning false.
    if DEBUG:
        print("[is_word_guessed](" + secret_word + ")")
    is_guessed = False
    if len(letters_guessed) == 0: # checks for edge case of no letters guessed
        return is_guessed
    for i in range(len(letters_guessed)):
        if secret_word[i] == letters_guessed[i]:
            pass
        else:
            return is_guessed
    is_guessed = True
    return is_guessed


def get_guessed_word(secret_word, letters_guessed):
    """
    A function that is used to get a string showing the letters guessed so far
    in the secret word and underscores for letters that have not been guessed
    yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been
        guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user
        has guessed correctly, the string should contain the letter at the
        correct position.  For letters in the word that the user has not yet
        guessed, shown an _ (underscore) instead.
    """
    if DEBUG:
        print("[get_guessed_word](" + secret_word +
              ")")
    # converts secret_word into a list
    final_output = list(secret_word)
    # turns final_output into a list full of blanks (underscores)
    for x in range(len(final_output)):
        final_output[x] = "_"
    # for every letter that has been guessed
    for x in range(len(letters_guessed)):
        # checks to see if it exists at an index y on secret_word
        for y in range(len(secret_word)):
            # if it exists at index y, then replaces at same index, with letter
            # that was tested, at final_output
            if letters_guessed[x] == secret_word[y]:
                final_output[y] = letters_guessed[x]
    # converts the list back to string
    return guessed_word_joinchar.join(final_output)


def is_guess_in_word(guess, secret_word):
    """
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    """
    # Checks to see if guess is at any index in the secret_word
    # otherwise returns False
    if DEBUG:
        print("[is_guess_in_word](" + guess + "," + secret_word + ")")
    for i in range(len(secret_word)):
        if guess == secret_word[i]:
            return True
        else:
            pass
    return False


def spaceman(secret_word):
    """
    A function that controls the game of spaceman. Will start spaceman in the
    command line.
    Args:
        secret_word (string): the secret word to guess.
    """

    # TODO: show the player information about the game according to the project
    # spec

    # TODO: Ask the player to guess one letter per round and check that it is
    # only one letter

    # TODO: Check if the guessed letter is in the secret or not and give the
    # player feedback

    # TODO: show the guessed word so far

    # TODO: check if the game has been won or lost
    try_again = True
    while try_again: # loop for playing again
        letters_guessed = list() #list of letters guessed
        guesses_left = 6 # guesses left, 0 means game over
        while (is_word_guessed(secret_word, letters_guessed) == False) and (guesses_left > 0): # game round loop. breaks if guesses run out or word is guessed.
            print("Word has not been guessed. Word state is:")
            preguess_state = get_guessed_word(secret_word, letters_guessed)
            print(preguess_state + "\n")

            user_input = input("Enter lowercase letter to guess: ")

            if is_guess_in_word(user_input, secret_word):
                letters_guessed.append(user_input)
            
            postguess_state = get_guessed_word(secret_word, letters_guessed)
            print(postguess_state + "\n")
            
            if preguess_state == postguess_state: # checks to see if the word has changed after the user has guessed the word (i.e. incorrect guess)
                print("Guessed incorrect letter.")
                -guesses_left # removes one guess
                print("You have " + str(guesses_left) + " guesses left")
            else:
                print("Guessed correctly.")
                print("You have " + str(guesses_left) + " guesses left")

        if guesses_left == 0:
            user_input = input("You have lost. Would you like to try again (y/n)?: ")
        else:
            user_input = input("You have won. Would you like to try again (y/n)?: ")

        if user_input == "y":
            try_again = True
        else:
            try_again = False

# Test functions
if TESTMODE:
    print("Testing with test variables:\n"
          "Secret word: " + TESTWORD + "\n"
          "Guessed word: " + TESTGUESSES + "\n"
          "Guessed letter: " + TESTGUESS + "\n"
          "Guessed letters(string): " + TESTLETTERSGUESSED
          )
    print("\n")

    print("Testing is_word_guessed:")
    print(is_word_guessed(TESTWORD, TESTGUESSES))
    print("\n")

    print("Testing is_guess_in_word:")
    print(is_guess_in_word(TESTGUESS, TESTWORD))
    print("\n")

    print("Testing get_guessed_word")
    print(get_guessed_word(TESTWORD, TESTLETTERSGUESSED))
    print("\n")


# These function calls that will start the game
if not TESTMODE:
    print("Starting game")
    secret_word = load_word()
    spaceman(secret_word)
