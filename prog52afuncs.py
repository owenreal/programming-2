import voidfunction

def calc_area(len, wid) -> int:
    return len * wid

def calc_perim(len: int, wid: int) -> int:
    return 2 * len + 2 * wid

def area_perim(len, wid):
    area = calc_area(len, wid)
    perim = calc_perim(len, wid)
    return area, perim

def main():
    voidfunction.do_thing()
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    a, p = area_perim(length, width)
    print(f"Area: {a}\nPerimeter: {p}")

if __name__ == "__main__":
    main()