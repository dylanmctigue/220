"""
Name: Dylan McTigue
lab10.py

Problem: Create the Button Class and Door Class that encapsulates data in a graphics window,
which allows the user to click the door and open and close it, then press exit when they want
to leave

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from button import Button
from door import Door
from graphics import GraphWin, Rectangle, Point

def main():
    win = GraphWin("lab 10", 500, 500)

    exit_button = Button(Rectangle(Point(100, 10), Point(400, 100)), "Exit")
    exit_button.color_button("blue")
    exit_button.draw(win)

    door = Door(Rectangle(Point(100, 150), Point(400, 475)), "Closed")
    door.color_door("red")
    door.draw(win)

    playing = True
    while playing:
        user_click = win.getMouse()

        click_door = door.is_clicked(user_click)

        if door.get_label() == 'Closed' and click_door:
            door.open("white", "Open")
        elif door.get_label() == 'Open' and click_door:
            door.close("red", "Closed")

        click_close = exit_button.is_clicked(user_click)
        if click_close:
            playing = False
    win.close()

main()