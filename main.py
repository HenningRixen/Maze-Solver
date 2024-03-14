from graphics import Window, Point, Line

def main():
    win = Window(800, 600)
    line = Line(Point(50,50), Point(400,400))
    line2 = Line(Point(500,500), Point(555,10))
    win.draw_line(line, "black")
    win.draw_line(line2, "red")
    win.wait_for_close()

main()
