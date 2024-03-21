from graphics import Line, Point


class Cell:
    def __init__(self, win=None):
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
        if self._win is None:
            return 
        
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
        if not self.has_top_wall:
            no_top_wall = Line(Point(_x1, _y1), Point(_x2, _y1))
            self._win.draw_line(no_top_wall, "sky blue")
        if self.has_right_wall:
            right_wall = Line(Point(_x2, _y1), Point(_x2, _y2))
            self._win.draw_line(right_wall)
        if self.has_bottom_wall:
            bottom_wall = Line(Point(_x1, _y2), Point(_x2, _y2))
            self._win.draw_line(bottom_wall)
        if not self.has_bottom_wall:
            no_bottom_wall = Line(Point(_x1, _y2), Point(_x2, _y2))
            self._win.draw_line(no_bottom_wall, "sky blue")

        
    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return 

        _x_middle = (self._x1 + self._x2)/ 2
        _y_middle = (self._y1 + self._y2)/ 2

        to_x_middle = (to_cell._x1 + to_cell._x2) / 2
        to_y_middle = (to_cell._y1 + to_cell._y2) / 2
        
        fill_color = "red"
        if undo:
            fill_color = "grey"
        
        #move left
        if self._x1 > to_cell._x1:
            line = Line(Point(self._x1, _y_middle), Point(_x_middle, _y_middle))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_middle, to_y_middle), Point(to_cell._x2, to_y_middle))
            self._win.draw_line(line, fill_color)
        
        #move right
        elif self._x1 < to_cell._x1:
            line = Line(Point(_x_middle, _y_middle), Point(self._x2, _y_middle))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_cell._x1, to_y_middle), Point(to_x_middle, to_y_middle))
            self._win.draw_line(line, fill_color)           
        
        #move up
        elif self._y1 > to_cell._y1:
            line = Line( Point(_x_middle, _y_middle), Point(_x_middle, self._y1),)
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_middle, to_cell._y2), Point(to_x_middle, to_y_middle))
            self._win.draw_line(line, fill_color)

        #move down
        elif self._y1 < to_cell._y1:
            line = Line(Point(_x_middle, _y_middle), Point(_x_middle, self._y2))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_middle, to_y_middle), Point(to_x_middle, to_cell._y1))
            self._win.draw_line(line, fill_color)

