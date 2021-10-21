import random
#initialize the variable under the import  
def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines() 
    f.close()
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:  = Arguments
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    for letter in secret_word: # [a_ _ a]  [] _ _ _ _ _ w a t e r 
        if letter not in letters_guessed:
            return False #ends the function and sends you to the top where I called the function for the for loop
    return True #Telling the computer that we won the game)

    # if len(set(secret_word)) == len(letters_guessed): #color , c o l r
    #     return True     #set <-  removes the duplicates ex: 10 A in the str, it will return 1 A 
    # return False

    # return True if len(set(secret_word)) == len(letters_guessed) else False
    # above function returns true if len(set(secret_word)) == len(letters_guessed)
    # returns false if len(set(secret_word)) == len (letters_guessed)

    #Computer to track on what is going on 
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    hidden_word = ""
    for char in secret_word: 
        if char in letters_guessed: 
            hidden_word += char
        else:
            hidden_word += "_"
    return hidden_word
            #   "water" w a t e r a _ _ _ a 
            #visual representation not tell you

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet



def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word
    
    if guess in secret_word:
        return True
    else:
        return False

# call the main function at the bottom so the helper functions can be used for main function

def spaceman(secret_word):
    ''' <- Description / for developers while # comment uses for yourself
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    #initializing 
    guesses = 7
    letter_guessed = []
    alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")
    #secret_word  = "water"

    #TODO: show the player information about the game according to the project spec
    print("Welcome to spaceman game")
    print(f"You only can guess one alphabet per round and you are only given {guesses} guesses per game")
    print(f"There are {', '.join(alphabet)} available to use and let's try it out!")
    print(get_guessed_word(secret_word, letter_guessed))
    #a__a __ answer    
    # True <- 5 == 5
    while True:
        # print(secret_word)
        print(f"Type any letter to guess the secret word")
        answer = input("> ").lower()

        if answer in letter_guessed:
            print("please type different alphabets that you have not used yet.")
        else:
            if is_guess_in_word(answer, secret_word):
                print(f"You found it! you have {guesses} more trial left")
                letter_guessed.append(answer)
            else:
                guesses -= 1
                print(f"Try it out again! you have {guesses} more trial left")

            # def get_guessed_word(secret_word, letters_guessed):
            
            print(get_guessed_word(secret_word, letter_guessed)) #Problem _ _ a _ _
            alphabet.remove(answer)
            print (f"{', '.join(alphabet)} available")
        
        if is_word_guessed(secret_word, letter_guessed):
            print("You won the game!")
            break
        elif guesses == 0:
            print("you lost the game!")
            break

#Usually George don't print out anything in the helper functions






# We cannot use the for loop because it counts the correct answer for the 7 guesses

#------------------------------start the program
# print(load_word())
secret_word = load_word() #secret_word is not equivalent to the one inside the load_word()'s secret_word because it is inside the scope.
spaceman(secret_word) #secret_word = random word
# the program starts from line 82 and any functions above the 82 are main, helper functions. 


#These function calls that will start the game
# secret_word = load_word()
# spaceman(secret_word)

# 1. Print the intro of the game including how many trials are available till the game ends and which alphabets are available to use.
# 2. Provide number of blank spaces that equivalents to the alphabet numbers for the solution of the word 
# 3. Provide an alphabet 
# 4. If it is correct then it fills up the blank space and display which alphabets are still available to use and how many trials are left. / 
#If it is wrong then it alerts the user that the alphabet they input was wrong and deduct 1 trial from the available trials.
# Display which alphabets are still available to use and how many trials are left. 
# 5. Print an alphabet
# 6. Show result
# 7. Print an alphabet 
# 8. ————————————continuing 
# 9. If the word is completed, print that you won the game./ If the word is not completed, print that you lost the game. 

