"""
Name: Dylan McTigue
lab6.py

Problem: Write a program to implement the Vigenere Cipher, where the user enters a message to code and a key,
and the program outputs a message using the key.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import GraphWin, Entry, Point, Text, Rectangle

def Vigenere():
    win = GraphWin("Vigenere", 500, 500)
    win.setCoords(0, 0, 10, 10)

    message_entry = Entry(Point(6, 7), 50)
    message_text = Text(Point(1, 7), "Message to Code: ")

    keyword_entry = Entry(Point(4, 5), 20)
    keyword_text = Text(Point(1, 5), "Enter Keyword: ")

    button = Rectangle(Point(4, 3), Point(6, 4))
    button_text_pt = Rectangle.getCenter(button)
    button_text = Text(button_text_pt, "Encode")

    message_entry.draw(win)
    message_text.draw(win)
    keyword_entry.draw(win)
    keyword_text.draw(win)
    button.draw(win)
    button_text.draw(win)

    win.getMouse()

    button.undraw()
    button_text.undraw()

    message = message_entry.getText()
    message = message.replace(" ", "")
    message = message.upper()

    keyword = keyword_entry.getText()
    keyword = keyword.replace(" ", "")
    keyword = keyword.upper()

    concatenation = ""

    message_length = len(message)
    keyword_length = len(keyword)

    for i in range(message_length):

        each_letter_message = message[i]
        each_letter_keyword = keyword[i % keyword_length]

        message_num = ord(each_letter_message)
        message_new_num = message_num - 65

        keyword_num = ord(each_letter_keyword)
        keyword_new_num = keyword_num - 65

        sum_num = message_new_num + keyword_new_num

        new_sum = sum_num % 26

        character = chr(new_sum + 65)

        concatenation = concatenation + character

    resulting_message = Text(Point(5, 2), "Resulting Message:")

    result_text = Text(Point(5, 1.5), "")
    result_text.draw(win)
    result_text.setText(concatenation)

    resulting_message.draw(win)

    click_to_close = Text(Point(5, 1), "Click to close window")
    click_to_close.draw(win)
    win.getMouse()
    win.close()
Vigenere()