"""
Name: Dylan McTigue
lab11.py

Problem: Using the Button and Door classes we made in lab last week, I need to create a game
that uses the graphics library to create three doors the user can click. Each round the
user can click one of those doors and possibly win if they select the secret door.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import Text, GraphWin, Rectangle, Point
from random import randint
from lab10.button import Button
from lab10.door import Door


def three_door_game():
    win = GraphWin("Three Door Game", 500, 500)

    quit_button = Button(Rectangle(Point(400, 25), Point(475, 100)), "Quit")
    quit_button.draw(win)

    wins_box = Rectangle(Point(25, 25), Point(75, 100))
    wins_box_center = wins_box.getCenter()
    wins_box.draw(win)

    losses_box = Rectangle(Point(75, 25), Point(125, 100))
    losses_box_center = losses_box.getCenter()
    losses_box.draw(win)

    wins_text = Text(Point(wins_box_center.getX(), wins_box_center.getY() - 45), "wins")
    wins_text.draw(win)

    losses_text = Text(Point(losses_box_center.getX(), losses_box_center.getY() - 45), "losses")
    losses_text.draw(win)

    wins = Text(wins_box_center, '0')
    wins.draw(win)

    losses = Text(losses_box_center, '0')
    losses.draw(win)

    door_1 = Door(Rectangle(Point(25, 150), Point(125, 400)), 'Door 1')
    door_1.color_door('brown')
    door_1.draw(win)

    door_2 = Door(Rectangle(Point(200, 150), Point(300, 400)), 'Door 2')
    door_2.color_door('brown')
    door_2.draw(win)

    door_3 = Door(Rectangle(Point(375, 150), Point(475, 400)), 'Door 3')
    door_3.color_door('brown')
    door_3.draw(win)

    secret_text = Text(Point(250, 100), 'I have a secret door')
    secret_text.draw(win)

    directions = Text(Point(250, 450), 'Click to guess which is the secret door!')
    directions.draw(win)

    count_wins = 0
    count_losses = 0
    user_click = win.getMouse()

    while not quit_button.is_clicked(user_click):
        secret_num = randint(1, 3)

        if secret_num == 1:
            door_1.set_secret(True)
            secret_door = door_1
        elif secret_num == 2:
            door_2.set_secret(True)
            secret_door = door_2
        else:
            door_3.set_secret(True)
            secret_door = door_3

        if door_1.is_clicked(user_click) and door_1.is_secret():
            door_1.color_door('green')
            secret_text.setText('you win!')
            count_wins = count_wins + 1
            wins.setText(str(count_wins))
        if door_1.is_clicked(user_click) and not door_1.is_secret():
            door_1.color_door('red')
            secret_text.setText('sorry, incorrect!')
            count_losses = count_losses + 1
            losses.setText(str(count_losses))
            secret_door.color_door('green')

        if door_2.is_clicked(user_click) and door_2.is_secret():
            door_2.color_door('green')
            secret_text.setText('you win!')
            count_wins = count_wins + 1
            wins.setText(str(count_wins))
        if door_2.is_clicked(user_click) and not door_2.is_secret():
            door_2.color_door('red')
            secret_text.setText('sorry, incorrect!')
            count_losses = count_losses + 1
            losses.setText(str(count_losses))
            secret_door.color_door('green')

        if door_3.is_clicked(user_click) and door_3.is_secret():
            door_3.color_door('green')
            secret_text.setText('you win!')
            count_wins = count_wins + 1
            wins.setText(str(count_wins))
        if door_3.is_clicked(user_click) and not door_3.is_secret():
            door_3.color_door('red')
            secret_text.setText('sorry, incorrect!')
            count_losses = count_losses + 1
            losses.setText(str(count_losses))
            secret_door.color_door('green')

        directions.setText('click anywhere to play again')

        user_click_two = win.getMouse()

        if quit_button.is_clicked(user_click_two):
            win.close()
        else:
            door_1.color_door('brown')
            door_2.color_door('brown')
            door_3.color_door('brown')

            door_1.set_secret(False)
            door_2.set_secret(False)
            door_3.set_secret(False)

            secret_text.setText('I have a secret door')
            directions.setText('Click to guess which is the secret door!')

            user_click = win.getMouse()

    win.close()

three_door_game()
