from code.main import Add

def TestAdd():
    assert Add(2.0,3.0) == 5.0
    assert Add(5.0, 5.0) == 10.0
    print("Add Function works correctly")


if __name__ == "__main__":
    TestAdd()