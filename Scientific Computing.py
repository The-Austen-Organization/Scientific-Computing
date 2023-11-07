import cmath
while True:
    try:
        print('Scientific Computing. \nPlease type in the entry box below the name of the following programs in brackets:')
        while True:
            print('>[Calculator]')
            print('>[Statistics]-Mean, Medium, Mode or Range')
            print('>[Probability]')
            print('>[Geometry]- Trigonometry and Spheres')
            print('>[File]-Opener, Histogram, Re-Writing')
            print('>[Fractions]')
            Program = input('What program are you going to use: ')
            Program = Program.lower()
            if Program == 'calculator':
                Number1 = float(input('First Number:'))
                Operator = input('Operator= +, -, x, /: ')
                Number2 = float(input('Second Number: '))
                if Operator == "+":
                    Answer = Number1 + Number2
                    print(str(Number1), Operator, str(Number2), '=', str(Answer))
                if Operator == "-":
                    Answer = Number1 - Number2
                    print(str(Number1), Operator, str(Number2), '=', str(Answer))
                if Operator == "x":
                    Answer = Number1 * Number2
                    print(str(Number1), Operator, str(Number2), '=', str(Answer))
                if Operator == "/":
                    Answer = Number1 / Number2
                    print(str(Number1), Operator, str(Number2), '=', str(Answer))
                if 'e' in str(Answer):
                    Tens = '0'
                    Answer = str(Answer).split('e')
                    Answer[1] = Answer[1][1:]
                    print((Answer[0].split('.')[0] + Answer[0].split('.')[1]) + (
                                (int(Answer[1]) - len(Answer[0].split('.')[1])) * '0'))
            elif Program == 'statistics':
                Statistics = input('Would you like mean, median, mode or range: ').lower()
                if Statistics == 'mean':
                    print('Enter the numbers in order the following way.\nEx: 23 34 45 23 34')
                    Mean = input('>').split()
                    MeanTotal = 0
                    for Number in Mean:
                        MeanTotal = MeanTotal + float(Number)
                    print(MeanTotal/len(Mean))
                if Statistics == 'median':
                    print('Enter the numbers in order the following way.\nEx: 23 34 45 23 34')
                    Median = input('>').split()
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
                if Statistics == 'mode':
                    ModeDict = dict()
                    print('Enter the numbers in order the following way.\nEx: 23 34 45 23 34')
                    Mode = input('>').split()
                    for Number in range(0, len(Mode)):
                        Mode[Number] = float(Mode[Number])
                    Mode.sort()
                    for Number in Mode:
                        ModeDict[Number] = ModeDict.get(Number, 0)+1
                    print(ModeDict)
                if Statistics == 'range':
                    print('Enter the numbers in order the following way.\nEx: 23 34 45 23 34')
                    Numbs = input('>').split()
                    for Range in range(0, len(Numbs)):
                        Numbs[Range] = float(Numbs[Range])
                    maximum = max(Numbs)
                    minimum = min(Numbs)
                    Total = maximum - minimum
                    print(Total)
            elif Program == 'probability':
                print('Choose:\n[Fractions]to percentages')
                Probability = input('What program do you what to use: ').lower()
                if Probability == 'fractions':
                    Numerator = float(input('What is the numerator: '))
                    Denominator = float(input('What is the Denominator: '))
                    print(Numerator / Denominator * 100, '%')
            elif Program == 'geometry':
                print('[Trigonometry]')
                print("[Trig-func]")
                Geometry = input('What program do you what to use: ').lower()
                if Geometry == 'trigonometry':
                    print('     /|')
                    print('    / |')
                    print('   /  |')
                    print(' h/   |a')
                    print(' /    |')
                    print('/_____|')
                    print('    b  ')
                    SideA = float(input('What is A: '))
                    SideB = float(input('What is B: '))
                    print(f"H is: {str((SideA**2  + SideB**2)**0.5)}")
                '''else Geometry == "trig-func":
                    pass'''
            elif Program == 'file':
                print('[Histogram]')
                FileProgram = input('What program do you what to use: ').lower()
                if FileProgram == 'histogram':
                    print("What mode do you want to use: Input or File? \nInput: You enter a line of text and then it\'s sorted \nFile: You choose a file to be sorted")
                    Options = input('>')
                    if Options.lower() == 'input':
                        counts = dict()
                        print('Enter a line of text:')
                        line = input('>')
                        words = line.split()
                        for word in words:
                            counts[word] = counts.get(word, 0) + 1
                        print('Counts', counts)
                        bigcount = None
                        bigword = None
                        for word, count in counts.items():
                            if bigcount is None or count > bigcount:
                                bigword = word
                                bigcount = count
                        print("Most counted word:", bigword, ",", bigcount)
                    elif Options.lower() == 'file':
                        print('Enter the file name:')
                        name = input('>')
                        handle = open(name)
                        counts = dict()
                        for line in handle:
                            words = line.split()
                            for word in words:
                                counts[word] = counts.get(word, 0) + 1
                        print('Counts', counts)
                        bigcount = None
                        bigword = None
                        for word, count in counts.items():
                            if bigcount is None or count > bigcount:
                                bigword = word
                                bigcount = count
                        print("Most counted word:", bigword, ",", bigcount)
                        handle.close()

            elif Program == 'fractions':
                try:
                    print('What program do you want?\nFractions(Add,Subtract,Multiply,Divide)\nMixedNumbers(With no space)')
                    Program = input('>')
                    if Program.lower() == 'fractions':
                        print('Enter Numerator one:')
                        Num1 = input('>')
                        Num1 = float(Num1)
                        print('Enter Denominator one:')
                        Den1 = input('>')
                        Den1 = float(Den1)
                        print('Enter Numerator two:')
                        Num2 = input('>')
                        Num2 = float(Num2)
                        print('Enter Denominator two:')
                        Den2 = input('>')
                        Den2 = float(Den2)
                        print('Enter the operator \n ex:Add(+)Subtract(-)Multiply(*)Divide(/)')
                        operator = input('>')
                        if operator == ('+'):
                            Num1 = Num1 * Den2
                            Num2 = Num2 * Den1
                            Den1 = Den1 * Den2
                            Den2 = Den2 * Den1
                            FinalNum = Num1 + Num2
                            FinalDen = Den1
                            FinalDec = FinalNum / FinalDen
                            print('The answer in fraction form is:', str(FinalNum) + '/' + str(FinalDen))
                            print('The answer in decimal form is:', str(FinalDec))
                        if operator == ('-'):
                            Num1 = Num1 * Den2
                            Num2 = Num2 * Den1
                            Den1 = Den1 * Den2
                            Den2 = Den2 * Den1
                            FinalNum = Num1 - Num2
                            FinalDen = Den1
                            FinalDec = FinalNum / FinalDen
                            print('The answer in fraction form is:', str(FinalNum) + '/' + str(FinalDen))
                            print('The answer in decimal form is:', str(FinalDec))
                        if operator == ('*'):
                            FinalNum = Num1 * Num2
                            FinalDen = Den1 * Den2
                            FinalDec = FinalNum / FinalDen
                            print('The answer in fraction form is:', str(FinalNum) + '/' + str(FinalDen))
                            print('The answer in decimal form is:', str(FinalDec))
                        if operator == ('/'):
                            FinalNum = Num1 * Den2
                            FinalDen = Num2 * Den1
                            FinalDec = FinalNum / FinalDen
                            print('The answer in fraction form is:', str(FinalNum) + '/' + str(FinalDen))
                            print('The answer in decimal form is:', str(FinalDec))
                    elif Program.lower() == 'mixednumbers':
                        print('Does one number have a mixed number or do both?(Type the number 1 or 2)')
                        Question1 = input('>')
                        Question1 = int(Question1)
                        if Question1 == 1:
                            print(
                                'Is the Fraction with the mixed number the first or the second one?(Type First or Second)')
                            Question2 = input('>')
                            if Question2.lower() == 'first':
                                print('Enter The Mixed Number:')
                                Mix = input('>')
                                Mix = float(Mix)
                                print('Enter Numerator one:')
                                Num1 = input('>')
                                Num1 = float(Num1)
                                print('Enter Denominator one:')
                                Den1 = input('>')
                                Den1 = float(Den1)
                                print('Enter Numerator two:')
                                Num2 = input('>')
                                Num2 = float(Num2)
                                print('Enter Denominator two:')
                                Den2 = input('>')
                                Den2 = float(Den2)
                                print('Enter the operator \nex:Add(+)Subtract(-)Multiply(*)Divide(/))')
                                operator = input('>')
                                if operator == ('+'):
                                    NewMix = Mix * Den1
                                    NewNum1 = NewMix + Num1
                                    NewNum1 = NewNum1 * Den2
                                    Num2 = Num2 * Den1
                                    Den1 = Den1 * Den2
                                    Den2 = Den2 * Den1
                                    FinalNum = NewNum1 + Num2
                                    FinalDen = Den1
                                    FinalDec = FinalNum / FinalDen
                                    print('The answer in fraction form is:', str(FinalNum) + '/' + str(FinalDen))
                                    print('The answer in decimal form is:', str(FinalDec))
                                if operator == ('-'):
                                    NewMix = Mix * Den1
                                    NewNum1 = NewMix + Num1
                                    NewNum1 = NewNum1 * Den2
                                    Num2 = Num2 * Den1
                                    Den1 = Den1 * Den2
                                    Den2 = Den2 * Den1
                                    FinalNum = NewNum1 - Num2
                                    FinalDen = Den1
                                    FinalDec = FinalNum / FinalDen
                                    print('The answer in fraction form is:', str(FinalNum) + '/' + str(FinalDen))
                                    print('The answer in decimal form is:', str(FinalDec))
                                if operator == ('*'):
                                    NewMix = Mix * Den1
                                    NewNum1 = NewMix + Num1
                                    NewNum1 = NewNum1 * Den2
                                    FinalNum = NewNum1 * Num2
                                    FinalDen = Den1 * Den2
                                    FinalDec = FinalNum / FinalDen
                                    print('The answer in fraction form is:', str(FinalNum) + '/' + str(FinalDen))
                                    print('The answer in decimal form is:', str(FinalDec))
                                if operator == ('/'):
                                    NewMix = Mix * Den1
                                    NewNum1 = NewMix + Num1
                                    FinalNum = NewNum1 * Den2
                                    FinalDen = Num2 * Den1
                                    FinalDec = FinalNum / FinalDen
                                    print('The answer in fraction form is:', str(FinalNum) + '/' + str(FinalDen))
                                    print('The answer in decimal form is:', str(FinalDec))
                            elif Question2.lower() == 'second':
                                print('Enter Numerator one:')
                                Num1 = input('>')
                                Num1 = float(Num1)
                                print('Enter Denominator one:')
                                Den1 = input('>')
                                Den1 = float(Den1)
                                print('Enter The Mixed Number:')
                                Mix = input('>')
                                Mix = float(Mix)
                                print('Enter Numerator two:')
                                Num2 = input('>')
                                Num2 = float(Num2)
                                print('Enter Denominator two:')
                                Den2 = input('>')
                                Den2 = float(Den2)
                                print('Enter the operator \nex:Add(+)Subtract(-)Multiply(*)Divide(/)')
                                operator = input('>')
                                if operator == ('+'):
                                    NewMix = Mix * Den2
                                    NewNum2 = NewMix + Num2
                                    NewNum2 = NewNum2 * Den1
                                    Num1 = Num1 * Den2
                                    Den1 = Den1 * Den2
                                    Den2 = Den2 * Den1
                                    FinalNum = Num1 + NewNum2
                                    FinalDen = Den1
                                    FinalDec = FinalNum / FinalDen
                                    print('The answer in fraction form is:', str(FinalNum) + '/' + str(FinalDen))
                                    print('The answer in decimal form is:', str(FinalDec))
                                if operator == ('-'):
                                    NewMix = Mix * Den2
                                    NewNum2 = NewMix + Num2
                                    NewNum2 = NewNum2 * Den1
                                    Num1 = Num1 * Den2
                                    Den1 = Den1 * Den2
                                    Den2 = Den2 * Den1
                                    FinalNum = Num1 - NewNum2
                                    FinalDen = Den1
                                    FinalDec = FinalNum / FinalDen
                                    print('The answer in fraction form is:', str(FinalNum) + '/' + str(FinalDen))
                                    print('The answer in decimal form is:', str(FinalDec))
                                if operator == ('*'):
                                    NewMix = Mix * Den2
                                    NewNum2 = NewMix + Num2
                                    FinalNum = Num1 * NewNum2
                                    FinalDen = Den1 * Den2
                                    FinalDec = FinalNum / FinalDen
                                    print('The answer in fraction form is:', str(FinalNum) + '/' + str(FinalDen))
                                    print('The answer in decimal form is:', str(FinalDec))
                                if operator == ('/'):
                                    NewMix = Mix * Den2
                                    NewNum2 = NewMix + Num2
                                    FinalNum = Num1 * Den2
                                    FinalDen = NewNum2 * Den1
                                    FinalDec = FinalNum / FinalDen
                                    print('The answer in fraction form is:', str(FinalNum) + '/' + str(FinalDen))
                                    print('The answer in decimal form is:', str(FinalDec))
                        elif Question1 == 2:
                            print('Enter The First Mixed Number:')
                            Mix1 = input('>')
                            Mix1 = float(Mix1)
                            print('Enter Numerator one:')
                            Num1 = input('>')
                            Num1 = float(Num1)
                            print('Enter Denominator one:')
                            Den1 = input('>')
                            Den1 = float(Den1)
                            print('Enter The Second Mixed Number:')
                            Mix2 = input('>')
                            Mix2 = float(Mix2)
                            print('Enter Numerator two:')
                            Num2 = input('>')
                            Num2 = float(Num2)
                            print('Enter Denominator two:')
                            Den2 = input('>')
                            Den2 = float(Den2)
                            print('Enter the operator \nex:Add(+)Subtract(-)Multiply(*)Divide(/)')
                            operator = input('>')
                            if operator == ('+'):
                                Mix1 = Mix1 * Den1
                                NewMix1 = Mix1 + Num1
                                Mix2 = Mix2 * Den2
                                NewMix2 = Mix2 + Num2
                                NewMix1 = NewMix1 * Den2
                                NewMix2 = NewMix2 * Den1
                                Den1 = Den1 * Den2
                                Den2 = Den2 * Den1
                                FinalNum = NewMix1 + NewMix2
                                FinalDen = Den1
                                FinalDec = FinalNum / FinalDen
                                print('The answer in fraction form is:', str(FinalNum) + '/' + str(FinalDen))
                                print('The answer in decimal form is:', str(FinalDec))
                            if operator == ('-'):
                                Mix1 = Mix1 * Den1
                                NewMix1 = Mix1 + Num1
                                Mix2 = Mix2 * Den2
                                NewMix2 = Mix2 + Num2
                                NewMix1 = NewMix1 * Den2
                                NewMix2 = NewMix2 * Den1
                                Den1 = Den1 * Den2
                                Den2 = Den2 * Den1
                                FinalNum = NewMix1 - NewMix2
                                FinalDen = Den1
                                FinalDec = FinalNum / FinalDen
                                print('The answer in fraction form is:', str(FinalNum) + '/' + str(FinalDen))
                                print('The answer in decimal form is:', str(FinalDec))
                            if operator == ('*'):
                                Mix1 = Mix1 * Den1
                                NewMix1 = Mix1 + Num1
                                Mix2 = Mix2 * Den2
                                NewMix2 = Mix2 + Num2
                                FinalNum = NewMix1 * NewMix2
                                FinalDen = Den1 * Den2
                                FinalDec = FinalNum / FinalDen
                                print('The answer in fraction form is:', str(FinalNum) + '/' + str(FinalDen))
                                print('The answer in decimal form is:', str(FinalDec))
                            if operator == ('/'):
                                Mix1 = Mix1 * Den1
                                NewMix1 = Mix1 + Num1
                                Mix2 = Mix2 * Den2
                                NewMix2 = Mix2 + Num2
                                FinalNum = NewMix1 * Den2
                                FinalDen = NewMix2 * Den1
                                FinalDec = FinalNum / FinalDen
                                print('The answer in fraction form is:', str(FinalNum) + '/' + str(FinalDen))
                                print('The answer in decimal form is:', str(FinalDec))
                    else:
                        print('This isn\'t a number (Only 1 and 2 are allowed)')
                except:
                    print('This isn\'t a float or a program\n Try Again')

            else:
                print("This program doesn't exist or it hasn't been created")
    except:
        print('This is a general error contact creators as a Humanoid.')
