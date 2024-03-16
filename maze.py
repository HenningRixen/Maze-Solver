from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        
        self._create_cells()
    
    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            column_cells = []
            for j in range(self.num_rows):
                cell = Cell(self.win)
                column_cells.append(cell)
            self._cells.append(column_cells)
        for i in range(self._num_cols):    
            for j in range(self.num_rows):
            self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        self.x1 = 0
        self.y1 = 0
        

