import random
# GLOBALS

# DEBUGGING GLOBALS
DEBUG = True
TESTWORD = "CAT"
TESTGUESS = "C_T"
TESTGUESSLETTER = "A"


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
        print("[is_word_guessed](" + secret_word + "," + letters_guessed + ")")
    is_guessed = False
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

    # TODO: Loop through the letters in secret word and build a string that
    # shows the letters that have been guessed correctly so far that are saved
    # in letters_guessed and underscores for the letters that have not been
    # guessed yet

    pass


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
    pass


# Test functions
if DEBUG:
    print("Testing with word " + TESTWORD + " and guess " + TESTGUESS)
    print("\n")

    print("Testing is_word_guessed:")
    print(is_word_guessed(TESTWORD, TESTGUESS))
    print("\n")

    print("Testing is_guess_in_word:")
    print(is_guess_in_word(TESTGUESSLETTER, TESTWORD))
    print("\n")


# These function calls that will start the game
secret_word = load_word()
spaceman(load_word())
