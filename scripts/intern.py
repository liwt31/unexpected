a = "__init__"
b = "__init__"
assert id(a) == id(b)


c = "__"
d = "init__"
assert id(a) == id(c+d)
