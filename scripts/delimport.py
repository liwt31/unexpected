class Foo:
    def __del__(self):
        import os


f = Foo()
