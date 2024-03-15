from graphics import Line, Point


class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, _x1, _y1, _x2, _y2):
        self._x1 = _x1
        self._x2 = _x2
        self._y1 = _y1
        self._y2 = _y2

        if self.has_left_wall:
            left_wall = Line(Point(_x1, _y1), Point(_x1, _y2))
            self._win.draw_line(left_wall)
        if self.has_top_wall:
            top_wall = Line(Point(_x1, _y1), Point(_x2, _y1))
            self._win.draw_line(top_wall)
        if self.has_right_wall:
            right_wall = Line(Point(_x2, _y1), Point(_x2, _y2))
            self._win.draw_line(right_wall)
        if self.has_bottom_wall:
            bottom_wall = Line(Point(_x1, _y2), Point(_x2, _y2))
            self._win.draw_line(bottom_wall)


