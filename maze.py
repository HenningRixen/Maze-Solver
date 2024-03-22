from cell import Cell
import random
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
    
    def _create_cells(self):
        
        for i in range(self._num_cols):
            column_cells = []
            for j in range(self._num_rows):
                cell = Cell(self._win)
                column_cells.append(cell)
            self._cells.append(column_cells)
        for i in range(self._num_cols):    
            for j in range(self._num_rows):
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
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            need_visit = []
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                need_visit.append((i - 1, j))
            #right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                need_visit.append((i + 1, j))
            #up
            if j > 0 and not self._cells[i][j - 1].visited:
                need_visit.append((i, j - 1))
            #down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                need_visit.append((i, j + 1))
            
            if len(need_visit) == 0:
                self._draw_cell(i, j)
                return
            
            # random direction
            direction = random.randrange(len(need_visit))
            next_step = need_visit[direction]

            #break left 
            if next_step[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            
            #break right 
            if next_step[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            
            #break up
            if next_step[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            
            #break down
            if next_step[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            
            self._break_walls_r(next_step[0], next_step[1])
            






