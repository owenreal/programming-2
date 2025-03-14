from cllp11 import PercentCalc


def main():

    print("CALCULATE YOUR TIME SPENT MAKING THE THING!")
    design = float(input("DESIGN TIME: "))
    code = float(input("CODE TIME: "))
    debug = float(input("DEBUG TIME: "))
    test = float(input("TEST TIME: "))
    fish = PercentCalc(design, code, debug, test)

    percents = PercentCalc.calc(fish)

    print("PERCENT OF TIME ON: DESIGNING, CODING, DEBUGGING, TESTING")
    print(percents)


if __name__ == "__main__":
    main()
