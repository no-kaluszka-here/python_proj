import sys
import random 

def game():

    # Play again?
    def play_again():
            again = input("Play again? (y/n): ")
            if again == 'n':
                print("Goodbye")
                sys.exit(0)     
            if again =='y':
                game()
            else:
                sys.exit(0)   

    # Choose a random line
    def random_line(fname):
        lines=open(fname).read().splitlines()
        return random.choice(lines)

    # Compare i/o
    def find_indexes(word, letter):
        indexes = []

        for index, letter_in_word in enumerate(word):
            if letter == letter_in_word:
                indexes.append(index)

        return indexes

    # Show state
    def show_state_of_game():
        print()
        print(user_word)
        print("Tries left: ", no_of_tires)
        print("Used letters: ", used_letters)
        print()

    no_of_tires=5
    word=random_line('list_game.txt')
    used_letters=[]
    user_word=[]

    ###

    for _ in word:
        user_word.append("_")

    while True:
        print(word)
        letter = input("Guess the letter: ")
        used_letters.append(letter)

        found_indexes = find_indexes(word,letter)

        if len(found_indexes) == 0:
            print("No such letter")
            no_of_tires-=1
            if no_of_tires==0:
                print("You lost")
                play_again()   
        else:
            for index in found_indexes:
                user_word[index]=letter

            if ("".join(user_word)) == word:
                print("You won")
                play_again()        
        show_state_of_game()
game()
