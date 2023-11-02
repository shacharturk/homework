from recursion_funcs import factorial, maze_solve
num = int(input("pleas enter a number: "))
print(f"the factorial of {num} is: {factorial(num)}")
print(maze_solve("maze.txt"))
