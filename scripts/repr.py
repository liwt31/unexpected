class A:
    def __repr__(self):
        True


a = A()


print(a.__repr__())  # ok
print(repr(a))  # fail
