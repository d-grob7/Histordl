import string
import words_test
import rich
from rich.prompt import Prompt
from rich.console import Console
from random import choice


def correct_place(letter):
    return f'[white on green]{letter}[/]'

def correct_letter(letter):
    return f'[white on yellow]{letter}[/]'

def incorrect(letter):
    return f'[black on white]{letter}[/]'




WELCOME_MESSAGE = correct_place("WELCOME TO HISTORDL")
INSTRUCTIONS = """This is a variation on WORDLE where A word having to do with this day in history has been randomly
selected. The number of tries you have to guess the word = the numbers of letters in the word + 1. 
So if the word selected has 6 letters, you get 7 tries to correctly guess the word. If you guessed a correct letter 
in the correct place, the letter will turn green. If you guessed a correct letter but in an incorrect place, 
the letter will turn yellow. If the letter you guessed is incorrect altogether, the letter will turn black. 
You may begin guessing. 
"""
remaining = [x for x in string.ascii_uppercase]


def display_guess(guess,answer,num_letters):
    display = []
    len_guessed = len(guess)

    if len_guessed != num_letters:
        print(f"You guessed {len_guessed} letters but your word has {num_letters} letters. Try again")


    else:
        for i, letter in enumerate(guess):
            if answer[i] == guess[i]:
                display += correct_place(letter)
            elif letter in answer:
                display += correct_letter(letter)
            else:
                display += incorrect(letter)

        return ''.join(display)


def letters_left(guess, answer,remaining):
    for i in guess:
        if i not in answer and i in remaining:
            remaining.remove(i)
    return remaining





def main():


    console = Console()
    console.print(WELCOME_MESSAGE)
    print(INSTRUCTIONS)

    game_word = choice(words_test.word_list).upper()
    #print(game_word) #for testing


    num_letters = len(game_word)
    allowed_guesses = num_letters + 1

    rich.print(f'The word you have to guess has {num_letters} letters')
    rich.print(f'you have {allowed_guesses} tries to guess the word')

    used_guesses = 0
    console.print(remaining)

    while used_guesses < allowed_guesses:
        used_guesses += 1
        player_guess = Prompt.ask("Enter your guess").upper()
        display = display_guess(player_guess, game_word, num_letters)

        if display == None:
            used_guesses -= 1
            continue

        else:
            console.print(display)
            console.print(letters_left(player_guess, game_word, remaining))


        if player_guess == game_word:
            break
    print(f"\n\nHISTORDL {used_guesses}/{allowed_guesses}\n")

















if __name__ == '__main__':
    main()