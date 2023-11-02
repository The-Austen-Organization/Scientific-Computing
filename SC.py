def cal(expr):
    Answer = eval(expr)
    print(Answer)
def mean(Mean):
    Mean = Mean.split()
    MeanTotal = 0
    for Number in Mean:
        MeanTotal = MeanTotal + float(Number)
    print(MeanTotal / len(Mean))
def median(Median):
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
    print(Median)
def mode(Mode):
    ModeDict = dict()
    Mode = Mode.split()
    for Number in range(0, len(Mode)):
        Mode[Number] = float(Mode[Number])
    Mode.sort()
    for Number in Mode:
        ModeDict[Number] = ModeDict.get(Number, 0) + 1
    print(ModeDict)
def Funrange(Numbs):
    Numbs = Numbs.split()
    for Range in range(0, len(Numbs)):
        Numbs[Range] = float(Numbs[Range])
    maximum = max(Numbs)
    minimum = min(Numbs)
    Total = maximum - minimum
    print(Total)
def percent(Numerator,Denominator):
    Numerator = float(Numerator)
    Denominator = float(Denominator)
    print(Numerator / Denominator * 100, '%')

