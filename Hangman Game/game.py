import random
WORD=["pakistan","india","bangale","england","Turkey"]
MAX_WRONG_GUESSES =6

HANGMANE_PICS=[
      r"""
      ___________
     |           |
     |
     |
     |
     |
     |
    _|___
    """,
    r"""
      ___________
     |           |
     |           O
     |
     |
     |
     |
    _|___
    """,
    r"""
      ___________
     |           |
     |           O
     |           |
     |           |
     |
     |
    _|___
    """,
    r"""
      ___________
     |           |
     |           O
     |          /|
     |           |
     |
     |
    _|___
    """,
    r"""
      ___________
     |           |
     |           O
     |          /|\
     |           |
     |
     |
    _|___
    """,
    r"""
      ___________
     |           |
     |           O
     |          /|\
     |           |
     |          /
     |
    _|___
    """,
    r"""
      ___________
     |           |
     |          \O/
     |          /|\
     |           |
     |          / \
     |    [ GAME OVER ]
    _|___
    """,
]

def choose_word():
    return random.choice(WORD)


def display_state(word,guessed_letters,wrong_guesses):
    print(HANGMANE_PICS[wrong_guesses])
    disply= ""
    for letter in word:
        if letter in guessed_letters:
            disply += letter + ""
        else:
            disply += "_"
    print("word:" + disply.strip())    # strip is used for removing the sapce of start and ending in this game
    print("Guessed letters:" +".join(sorted(guessed_letters))" if guessed_letters else "Guessed letters: none")
    print(f"wrong guesses: {wrong_guesses}/{MAX_WRONG_GUESSES}")


def get_guess(guessed_letters):
    while True:
        raw=input("Guess a letter:")

        guess= " ".join(ch for ch in raw if ch.isalpha()).lower()
        if len(guess)!=1:
            print("please enter a single letter (you enter:{raw!r}).")
        elif guess in guessed_letters:
            print("you already guessed that letter.Try again.")
        else:
            return guess
                           #GAME WIN CONDITIONS
def play_game():
    word= choose_word()
    guessed_letters=[]
    wrong_guesses=0

    print("Well come to hangmen game")
    print(f"Try to guess the word.you have {MAX_WRONG_GUESSES} incorrect guesses allowed.\n")


    while wrong_guesses < MAX_WRONG_GUESSES:
        display_state(word,guessed_letters ,wrong_guesses)


        if all(letter in guessed_letters for letter in word):
            print(f"\n congraultion you guessed the word:{word} ")
            return


        guess=get_guess(guessed_letters)
        guessed_letters.append(guess)  


        if guess in word:
            print("correct!\n")
        else:
            wrong_guesses +=1
            print("wrong guess!\n")

            # PLAYER LOST GAME
    
    display_state(word,guessed_letters,wrong_guesses)
    print(f"\n Game over ! you ran out of guesses.The word was:{word}")


def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").lower().strip()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
