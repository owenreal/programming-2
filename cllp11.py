class PercentCalc:
    def __init__(self, design, code, debug, test):
        self.design = design
        self.code = code
        self.debug = debug
        self.test = test
        self.total = 0.0

    def calc(self):
        self.total = self.design + self.code + self.debug + self.test
        designper = self.design / self.total * 100
        codeper = self.code / self.total * 100
        debugper = self.debug / self.total * 100
        testper = self.debug / self.total * 100

        percents = [round(designper, 2), round(codeper, 2), round(debugper, 2), round(testper, 2)]
        return percents
