class math():
    """
    ##############################
    This is the math documentation
    ##############################

    This class has methods that do math.

    """
    def cal(self, expr: str) -> float:
        """
        Evaluate mathematical expressions.
        """
        return float(eval(expr))
    
    def mean(self, Mean: list) -> float:
        """
        Calculate the arithmetic mean.
        """
        Mean = Mean.split()
        MeanTotal = 0
        for Number in Mean:
            MeanTotal = MeanTotal + float(Number)
        return MeanTotal / len(Mean)
    
    def median(self, Median: list) -> float:
        """
        Calculates the median value of a list.
        """
        Median = Median.split()
        for Number in range(0, len(Median)):
            Median[Number] = int(Median[Number])
        MedianLen = len(Median)
        Median.sort()
        if MedianLen % 2 == 0:
            Median1 = Median[MedianLen // 2]
            Median2 = Median[MedianLen // 2 - 1]
            Median = (Median1 + Median2) / 2
        else:
            Median = Median[MedianLen // 2]
        return float(Median)
    
    def mode(self, Mode: list) -> dict:
        """
        Calculates the mode.
        """
        ModeDict = dict()
        Mode = Mode.split()
        for Number in range(0, len(Mode)):
            Mode[Number] = float(Mode[Number])
        Mode.sort()
        for Number in Mode:
            ModeDict[Number] = ModeDict.get(Number, 0) + 1
        return ModeDict
    
    def math_range(self, Numbs: list) -> float:
        """
        Gets the mathematical range, so largest numbers - smallest number.
        """
        Numbs = Numbs.split()
        for Range in range(0, len(Numbs)):
            Numbs[Range] = float(Numbs[Range])
        maximum = max(Numbs)
        minimum = min(Numbs)
        Total = maximum - minimum
        return float(Total)
    
    def fraction_to_percent(self, Numerator: float, Denominator: float) -> tuple:
        """
        Turns a fraction into a percentage.
        """
        return (str(Numerator / Denominator * 100) + '%', Numerator / Denominator * 100)
    class geometry():
        def pythagorean_theorem(self, a, b):



