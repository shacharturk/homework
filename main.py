from bin_node import bin_node
from bin_node_functions import how_many, are_all, is_pallindrom, compressed, decompressed

val = "a"
tree = bin_node("a", bin_node("b", bin_node("c")), bin_node("h", bin_node("b")))
print(how_many(tree, val))
print(are_all(tree, "ach"))
print(is_pallindrom(tree))
compressed(tree)
result = open("result.txt", "r")
txt = result.read()
result.close()
print(txt)
print(decompressed(txt).get_left().get_value())