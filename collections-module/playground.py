from collections import ChainMap

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
d4 = {'g': 7, 'h': 8}

chainmap = ChainMap(d1, d2, d3)

print(chainmap.new_child(d4))
print(chainmap)
