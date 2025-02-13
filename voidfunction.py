from calcfunctions import *

def do_thing():
    print("hello")

def print_nums() -> None:
    for i in range(10+1):
        print("i:", i)
    pass

def main():
    do_thing()
    print_nums()
    a = add(1, 2)
    q, r = divmod2(5, 10)
    print(q, r)

if __name__ == "__main__":
    main()