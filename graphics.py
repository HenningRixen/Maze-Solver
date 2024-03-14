from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, width=width, height=height, bg="sky blue")
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        
    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("window closed")
        
    def close(self):
        self.running = False
    
    def draw_line(self, class_line_instance, fill_color = "black"):
        class_line_instance.draw(self.canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, class_point1_instance, class_point2_instance):
        self.class_point1_instance = class_point1_instance
        self.class_point2_instance = class_point2_instance
    
    def draw(self, canvas, fill_color = "black"):
        canvas.create_line(self.class_point1_instance.x, self.class_point1_instance.y, self.class_point2_instance.x, self.class_point2_instance.y, fill=fill_color, width=2)
        canvas.pack(fill=BOTH, expand=1)
    





