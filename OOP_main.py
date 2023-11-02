import quad_implementation
s = quad_implementation.Square(5)
r = quad_implementation.Rectangle(8, 2)

print(f"square area = {s.get_area()}")
print(f"rectangle area = {r.get_area()}")
print(f"aggregated area is: {s+r}")
