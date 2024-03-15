from graphics import Window
from cell import Cell

def main():
    win = Window(800, 600)

    c = Cell(win)
    c.has_left_wall = False
    c.draw(50, 50, 120, 120)

    c = Cell(win)
    c.has_top_wall = False
    c.draw(150, 150, 200, 200)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(250, 250, 275, 275)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(300, 300, 500, 500)



    
    

    win.wait_for_close()

main()
