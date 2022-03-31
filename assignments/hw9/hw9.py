"""
Name: Dylan McTigue
hw9.py

Problem: Create functions that read and write files, use conditionals, and use
decision structures and repetition structures. The functions can play hangman.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint
from graphics import GraphWin, Point, Entry, Text, Circle, Line

def get_words(file_name):
    in_file = open(file_name, 'r')
    read_file = in_file.readlines()
    return read_file


def get_random_word(words):
    rand_word = words[randint(0, len(words) - 1)]
    new_word = rand_word.replace("\n", "")
    return new_word


def letter_in_secret_word(letter, secret_word):
    letters_in_word = secret_word.count(letter)
    return letters_in_word > 0


def already_guessed(letter, guesses):
    guessed_already = False
    for i in guesses:
        if i == letter:
            guessed_already = True
    return guessed_already


def make_hidden_secret(secret_word, guesses):
    letter_list = list(secret_word)
    for i in range(len(letter_list)):
        letter_list[i] = "_"

    for j in range(len(secret_word)):
        for guessed_letter in guesses:
            if secret_word[j] == guessed_letter:
                letter_list[j] = guessed_letter
    result = " ".join(letter_list)

    return result


def won(guessed):
    underscore_num = guessed.count("_")
    return not underscore_num > 0


def play_graphics(secret_word):
    guesses_left = 6
    guesses = []
    playing = True

    win = GraphWin("Hangman", 700, 700)
    win.setCoords(0, 0, 10, 10)

    bottom = Line(Point(6, 3.5), Point(9, 3.5))
    bottom.draw(win)

    post = Line(Point(7.5, 3.5), Point(7.5, 7.5))
    post.draw(win)

    horizontal_line = Line(Point(7.5, 7.5), Point(5, 7.5))
    horizontal_line.draw(win)

    rope = Line(Point(5, 7.5), Point(5, 6.5))
    rope.draw(win)

    letter_entry = Entry(Point(5, 2), 10)
    letter_entry.draw(win)

    entry_text = Text(Point(3.5, 2), "Guess a letter:")
    entry_text.draw(win)

    secret_word_text = Text(Point(5, 3), make_hidden_secret(secret_word, guesses))
    secret_word_text.draw(win)

    letters_guessed = Text(Point(5, 8.5), "Already guessed:")
    letters_guessed.draw(win)

    guesses_left_text = Text(Point(5, 9), "Guesses Left: {}".format(guesses_left))
    guesses_left_text.draw(win)

    while playing:

        letters_guessed.setText("Already guessed: {}".format(guesses))
        secret_word_text.setText(make_hidden_secret(secret_word, guesses))
        guesses_left_text.setText("Guesses Left: {}".format(guesses_left))

        win.getMouse()
        answer = letter_entry.getText()

        if not already_guessed(answer, guesses):
            guesses = guesses + [answer]
            if not letter_in_secret_word(answer, secret_word):
                guesses_left = guesses_left - 1

                if guesses_left == 5:
                    head = Circle(Point(5, 6), 0.5)
                    head.draw(win)
                if guesses_left == 4:
                    body = Line(Point(5, 5.5), Point(5, 4.5))
                    body.draw(win)
                if guesses_left == 3:
                    right_leg = Line(Point(5, 4.5), Point(5.5, 4))
                    right_leg.draw(win)
                if guesses_left == 2:
                    left_leg = Line(Point(5, 4.5), Point(4.5, 4))
                    left_leg.draw(win)
                if guesses_left == 1:
                    right_arm = Line(Point(5, 5), Point(5.5, 5.25))
                    right_arm.draw(win)
                if guesses_left == 0:
                    left_arm = Line(Point(5, 5), Point(4.5, 5.25))
                    left_arm.draw(win)

        letter_entry.setText("")

        if guesses_left == 0 and not won(make_hidden_secret(secret_word, guesses)):
            playing = False

            letter_entry.undraw()
            entry_text.undraw()

            losing_text = Text(Point(5, 2), "Sorry, you did not get the word")
            losing_text.draw(win)

            correct_word = Text(Point(5, 1.5), "The correct word was {}".format(secret_word))
            correct_word.draw(win)

            guesses_left_text.setText("Guesses Left: {}".format(guesses_left))

            win.getMouse()
            win.close()

        else:
            playing = True

        if won(make_hidden_secret(secret_word, guesses)):
            playing = False

            entry_text.undraw()

            winning_text = Text(Point(5, 1), "Winner!")
            winning_text.draw(win)

            secret_word_text.setText(make_hidden_secret(secret_word, guesses))

            win.getMouse()
            win.close()



def play_command_line(secret_word):
    guesses_left = 6
    guesses = []
    playing = True

    while playing:
        print("already guessed:", guesses)
        print("guesses remaining: {}".format(guesses_left))
        print(make_hidden_secret(secret_word, guesses))
        answer = input('guess a letter: ')
        print()

        if not already_guessed(answer, guesses):
            guesses = guesses + [answer]
            if not letter_in_secret_word(answer, secret_word):
                guesses_left = guesses_left - 1

        if guesses_left == 0 and not won(make_hidden_secret(secret_word, guesses)):
            playing = False
            print('Sorry, you did not guess the word. The secret word was {}'.format(secret_word))
        else:
            playing = True

        if won(make_hidden_secret(secret_word, guesses)):
            print('winner!')
            print(secret_word)
            playing = False


if __name__ == '__main__':
    secret_word = get_random_word(get_words('words.txt'))
    play_command_line(secret_word)
    # play_graphics(secret_word)
