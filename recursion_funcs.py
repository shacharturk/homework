def factorial(n):
  if n==0:
    return 1
  return n*factorial(n-1)


def maze_solve(file_name):
    path = []
    x, y = 0, 0
    f = open(file_name, 'r')
    maze = f.read()
    maze = maze.splitlines()
    f.close()

    def explore(maze, x, y, path):
        path += [(x, y)]

  #'y' is before 'x' because it is a list of the lines, which represent the y, and than a string of chars, which are x
        if y == len(maze)-1 and x == len(maze[y])-1:#stopping condition
            return True, path

        if x<len(maze[y])-1:  #going right
            right = maze[y][x+1]
            if int(right) and not (x+1, y) in path:
                return explore(maze, x+1, y, path)

        if y<len(maze)-1:#going down
            down = maze[y+1][x]
            if int(down) and not (x,y+1) in path:
                return explore(maze, x, y+1, path)

        if y > 0:#going up
            up = maze[y-1][x]
            if up and ((x, y-1) not in path):
                return explore(maze, x, y-1, path)
        if x>0:#going left
            left = maze[y][x-1]
            if int(left) and not (x-1, y) in path:
                return explore(maze, x-1, y, path)
        return False,path
    return explore(maze, 0, 0, path)
