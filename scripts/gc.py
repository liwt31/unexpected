class A:
    def __del__(self):
        assert False

def foo():
    a = A()
    del a
    print("ignored exception!")

foo()
