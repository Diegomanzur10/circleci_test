import code.main as main

def TestAdd():
    assert main.Add(2.0,3.0) == 5.0
    print("Add Function works correctly")


if __name__ == "__main__":
    TestAdd()