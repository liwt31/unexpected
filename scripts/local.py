globals()["i"] = 1
print(i)  # ok


def foo():
    print(i)  # fail
    i = 1


foo()
