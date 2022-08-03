"""
Maze visualizer 

@author: Daniel Bauer 
"""

from tkinter import *
import random


def make_empty_maze(width, height, walls = False): 
  maze = {}
  for row in range(height): 
    for column in range(width): 
      if walls: 
        maze[(row, column)] = [1,1,1,1]
      else: 
        maze[(row, column)] = [0,0,0,0]

  return maze

def make_simple_maze(width, height, n = 10):
  maze = make_empty_maze(width, height)

  obstacles = set()  
  while len(obstacles) < n: #Makes n walls
    i = random.randint(0,height-1)
    j = random.randint(0,width-1)

    if not (i,j) in obstacles: 
      obstacles.add((i,j))
      # make wall 
      maze[(i,j)] = [1,1,1,1]
      if i > 0:
        maze[(i-1, j)][3] = 1
      if i < height-1: 
        maze[(i+1, j)][1] = 1
      if j > 0: 
        maze[(i, j-1)][2] = 1
      if j < width-1: 
        maze[(i, j+1)][0] = 1
  return maze


def make_maze(width, height):
  x = 0
  y = 0 
  maze = make_empty_maze(width, height, walls = True)  
  backtrack = []
  visited = 1
  current_cell = (y, x)
  while (visited <(height*width)):
    # Get unvisited neighbors using nearby
    nearby_list = nearby(maze, height, width, current_cell[0], current_cell[1])
    if len(nearby_list) > 0:
      next_cell = random.randint(0, (len(nearby_list)-1))
      next_cell = nearby_list[next_cell]
      remove_wall(maze, current_cell, next_cell)
      backtrack.append(current_cell)
      backtrack.append(next_cell)
      current_cell = next_cell
      visited += 1

    else: current_cell = backtrack.pop()
  
  return maze

def all_walls(maze, y, x): #Unvisited if has all four walls
  if maze[(y,x)][0] == 1 and maze[(y,x)][1] == 1 and maze[(y,x)][2] == 1 and maze[(y,x)][3] == 1: #maze[coordinate][->] -> 0 (west), 1(north), 2(east), 3(south)
    return True
  else:
    return False

def nearby(maze, height, width, y, x): # Returns list of all possible options
  nearby_list = []
  if x > 0 and all_walls(maze, y, x-1) == True:
    nearby_list.append((y, x-1))
  if y > 0 and all_walls(maze, y-1, x) == True:
    nearby_list.append((y-1, x))
  if x < (width-1) and all_walls(maze,y, x+1) == True:
    nearby_list.append((y, x+1))
  if y < (height-1) and all_walls(maze, y+1, x) == True:
    nearby_list.append((y+1, x))
  return nearby_list

def remove_wall(maze, current_cell, next_cell): #maze[coordinate][->] -> 0 (west), 1(north), 2(east), 3(south)
  if current_cell[0] == next_cell[0]: #Neighbor is on the right
    if current_cell[1] < next_cell[1]:
      maze[current_cell][2] = 0
      maze[next_cell][0] = 0
    elif current_cell[1] > next_cell[1]: #Neighbor is on the left
      maze[current_cell][0] = 0 
      maze[next_cell][2] = 0
  else:
    if current_cell[0] < next_cell[0]: #Neighbor is down
      maze[current_cell][3] = 0
      maze[next_cell][1] = 0
    elif current_cell[0] > next_cell[0]: #Neighbor is up
      maze[current_cell][1] = 0
      maze[next_cell][3] = 0
 
def get_neighbors(maze,height,width,y, x): #maze[coordinate][->] -> 0 (west), 1(north), 2(east), 3(south)
  neighbors = []
  if x > 0 and maze[(y,x)][0]==0: 
    neighbors.append((y,x-1))
  if y > 0 and maze[(y,x)][1]==0:
    neighbors.append((y-1,x))
  if x < width-1 and maze[(y,x)][2]==0:
    neighbors.append((y,x+1))
  if y < height-1 and maze[(y,x)][3]==0:
    neighbors.append((y+1,x))
  return neighbors
        

class MazeVisualizer(object): #Change appeareance of maze

    def __init__(self): 

      self.offset = 0 
      self.cell_size = 50 #Each square size | default 50
      self.height = 20 
      self.width = 20 #Change these to make maze bigger/smaller | default 20

      root = Tk()
      root.wm_title("Maze simulator")
      root.lift()
      root.attributes("-topmost", True)
      self.root = root
      self.canvas = Canvas(root,height = self.cell_size * self.height, width = self.cell_size * self.width, borderwidth=0, highlightthickness=0)
      self.canvas.pack()

    def draw_grid(self):
      for i in range(self.height):
        for j in range(self.width):
          self.canvas.create_rectangle(j*self.cell_size, i*self.cell_size, (j+1)*self.cell_size, (i+1)*self.cell_size, outline="gray", fill="white") 
      

    def draw_maze(self, maze):
      self.canvas.create_rectangle(0,0,self.width * self.cell_size-1, self.height * self.cell_size-1, outline="black") # outline

      for i in range(self.height): 
        for j in range(self.width): 
          cell = maze[(i,j)]
          if cell[0]: self.canvas.create_line(j*self.cell_size, i*self.cell_size, j*self.cell_size, (i+1)*self.cell_size, width=2)    # left
          if cell[1]: self.canvas.create_line(j*self.cell_size, i*self.cell_size, (j+1)*self.cell_size, i*self.cell_size, width=2)    # up 
          if cell[2]: self.canvas.create_line((j+1)*self.cell_size, i*self.cell_size, (j+1)*self.cell_size, (i+1)*self.cell_size, width=2)    # right  
          if cell[3]: self.canvas.create_line(j*self.cell_size, (i+1)*self.cell_size, (j+1)*self.cell_size, (i+1)*self.cell_size, width=2)    # down

     
    def bfs_step(self, maze, goal):
      if self.queue:
        u = self.queue.pop(0)
        if not u in self.visited: 

          self.paint_cell(u[0], u[1], "gray")
          self.visited.add(u)
          discovered_now = set()
          for v in get_neighbors(maze, self.height, self.width, u[0], u[1]):
            discovered_now.add(v)
            if not v in self.discovered:
              self.prev[v] = u
              self.discovered.add(v)
              self.queue.append(v) 
              if v == goal: 
                # Draw path
                self.draw_path(goal)
                return

          self.paint_set(self.queue, "green")
          self.root.after(50, lambda: self.bfs_step(maze,goal))
          

    def bfs_visualizer(self, maze, start, goal):
      self.prev = {}
      self.draw_maze(maze)
        
      self.paint_cell(start[0], start[1], "red")
      self.paint_cell(goal[0], goal[1], "black")

      self.queue = [start]
      self.discovered = set([start])

      self.visited = set()
      self.root.after(50, lambda: self.bfs_step(maze,goal))

    def draw_path(self, goal): 
      curr = goal
      begin = curr
      while curr in self.prev: 
        self.paint_cell(curr[0], curr[1], "blue") #paint path blue
        curr = self.prev[curr]
      self.paint_cell(curr[0], curr[1], "purple") #paint starting cell 
      curr = begin
      self.paint_cell(curr[0], curr[1], "green") #paint ending cell
    def dfs_step(self, maze,goal):
      if self.stack:
        u = self.stack.pop()
        if not u in self.visited: 

          self.paint_cell(u[0], u[1], "gray")
          self.visited.add(u)
          neighbors = get_neighbors(maze, self.height, self.width, u[0], u[1])
          random.shuffle(neighbors)
          for v in neighbors: 
            if not v in self.discovered:
              self.prev[v] = u
              self.paint_cell(v[0], v[1], "black") #paint current procesing cell
              self.discovered.add(v)
              self.stack.append(v) 
              if v == goal: 
                self.draw_path(goal) 
                return

          self.root.after(50, lambda: self.dfs_step(maze,goal))
          
    def dfs_visualizer(self, maze, start, goal):
      self.prev = {}
      self.draw_maze(maze)
        
      self.paint_cell(start[0], start[1], "red")
      self.paint_cell(goal[0], goal[1], "green") #paint goal

      self.stack= [start]
      self.discovered = set([start])

      self.visited = set()
      self.root.after(50, lambda: self.dfs_step(maze,goal))
  
    def paint_cell(self,y,x, color): 
      self.canvas.create_oval(self.cell_size * x+5, self.cell_size * y+5, self.cell_size* (x+1)-5, self.cell_size * (y+1)-5, fill=color, outline=color)
      
    def paint_set(self, coordinate_set, color):
      for (y,x) in coordinate_set: 
        self.paint_cell(y,x, color)

    def run(self):
      #maze = make_simple_maze(self.height, self.width, 80) 
      #maze = make_empty_maze(self.height, self.width, walls = True) 
      #maze = make_simple_maze(self.height, self.width, 80)
      maze = make_maze(self.width, self.height)
      self.draw_maze(maze)
      self.dfs_visualizer(maze, (0,0), (self.height-1, self.width-1)) #Choose bfs or dfs for different searching algoritms
      self.canvas.mainloop()
 
def main():
  gui = MazeVisualizer()
  gui.run()

if __name__ == "__main__":
  main()
