from cell import Cell
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        
        self._create_cells()
    
    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            column_cells = []
            for j in range(self.num_rows):
                cell = Cell(self._win)
                column_cells.append(cell)
            self._cells.append(column_cells)
        for i in range(self.num_cols):    
            for j in range(self.num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return 
        
        x_pos = self.x1 + i * self.cell_size_x
        y_pos = self.y1 + j * self.cell_size_y
        x2_pos = x_pos + self.cell_size_x
        y2_pos = y_pos + self.cell_size_y
        
        self._cells[i][j].draw(x_pos, y_pos, x2_pos, y2_pos)
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return         
        self._win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit():
        



