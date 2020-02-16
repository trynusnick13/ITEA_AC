from contextlib import contextmanager

@contextmanager
def open_file():
    print("Start")
    yield
    print("finish")

with open_file() as a:
    with open_file() as b:
        print("Second indent")
    print("indent finish")
print("End")
