def hangman(word):
    wrong = 0
    stages = ["",
              "________________                ",
              "|                               ",
              "|                |              ",
              "|                o              ",
              "|               /|\             ",
              "|               / \             ",
              "|                               "]
    lettersInWord = list(word)
    board = ["__"]*len(word)
    win = False
    print("welcome to Hangman")
    while wrong < len(stages) - 1:
        print()
        message = "Guess a letter:"
        guessedLetter = input(message)
        if guessedLetter in lettersInWord:
            index = lettersInWord.index(guessedLetter)
            board[index] = guessedLetter
            lettersInWord[index] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "__" not in board:
            print("you win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! It was {}.".format(word))

hangman("cat")
            
