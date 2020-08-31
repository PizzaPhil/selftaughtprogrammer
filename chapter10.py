# hangman
import random

wordlist = ["dance","skip","jump","shark","dog","cat","lisa","robot","chair","turtle"]
word = wordlist[random.randrange(len(wordlist))]

def hangman(word) :
    wrong = 0
    stages = ["",
            "________ ",
            "| ",
            "|    | ",
            "|    0 ",
            "|   /|\ ",
            "|   / \ ",
            "| " ]

    rletters = list(word)
    board = (["_"] * len(word))
    win = False
    print("Welcome to Hangman")

    while wrong < (len(stages) - 1) :
        print("\n")
        msg = "Guess a Letter: "
        char = input(msg)
        if char in rletters :
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else :
            wrong += 1

        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))

        if "_" not in board :
            print("you win!")
            print(" ".join(board))
            win = True
            break
    if not win :
        print("\n".join(stages[0:wrong]))
        print("you lose! it was {}.".format(word))

hangman(word)
