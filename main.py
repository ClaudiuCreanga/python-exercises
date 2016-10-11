def print_range():
    numbers = [i for i in range(2000,3201)]
    for i in numbers:
        if i % 7 == 0:
            if i % 5 != 0:
                print str(i)+",",
#print print_range()

def get_factorial(number):
    result = 1
    for x in range(2,number+1):
        result *= x
    return result
#print get_factorial(8)

def new_factorial(number):
    if number == 1:
        return 1
    return number * new_factorial(number - 1)
#print new_factorial(8)

def dictionary_generate(x):
    d = {i:i*i for i in range(1,x+1)}
    return d
#print dictionary_generate(8)

def change_type():
    x = raw_input("Type a list of comma sepparated numbers")
    x = x.split(",")
    new_tuple = tuple(x)
    return x
    #return new_tuple
#print change_type()

class Format_String(object):
    def __init__(self):
        self.input = self.getString()
        self.printString()
    def getString(self):
        input = raw_input("Please type a string: ")
        return input
    def printString(self):
        print self.input.upper()
#my_string = Format_String()

def square_root():
    x = raw_input("Please insert values comma separated: ")
    x = x.split(",")
    for i in x:
        i = int(i)
        print int(((2 * 50 * i) / 30) ** 0.5),
#square_root()

def matrix():
    x = raw_input("Two numbers commma separated: ")
    items =[int(i) for i in x.split(",")]
    Matrix = [[n*i for n in range(items[1])] for i in range(items[0])]
    print Matrix
#matrix()

def comma_words():
    x = raw_input("A list of comma separated words which will be sorted alphabetically: ")
    x = x.split(",")
    print ",".join(sorted(x))
#comma_words()

def capitalize_multiple_lines():
    x = '\n'.join(iter(raw_input, "done"))
    print x.upper(),
#capitalize_multiple_lines()

#or 
def multiple_lines():
    lines = []
    while True:
        s = raw_input()
        if s:
            lines.append(s.upper())
        else:
            break;
    for sentence in lines:
        print sentence
#multiple_lines()

def remove_duplicates_and_sort():
    x = raw_input("Your string: ")
    x = sorted(x.split(" "))
    new_line = []
    for i in x:
        if i not in new_line:
            new_line.append(i)
    print " ".join(new_line)
#remove_duplicates_and_sort()
#or use set() to remove duplicates

def divisible_by_five():
    x = raw_input("give 4 digit binary numbers comma separated: ")
    x = x.split(",")
    new_list = []
    for i in x:
        if int(i) % 5 == 0:
            new_list.append(i)
    print ",".join(new_list)
#divisible_by_five()

def each_digit_even_number():
    x = [x for x in range(2000,3001)]
    new_list = []
    for i in x:
        for n in str(i):
            a = 0
            if int(n) % 2 != 0:
                a = 1
                break
        if a != 1:
            new_list.append(str(i))
    print ",".join(new_list)
#each_digit_even_number()

def number_letters_digits():
    x = raw_input("Letters and digits: ")
    letters = 0
    digits = 0
    for i in x:
        if i.isalpha():
            letters += 1
        elif i.isdigit():
            digits += 1
    print "LETTERS "+str(letters)
    print "DIGITS "+str(digits)
#number_letters_digits()

def find_uppercase():
    x = raw_input("Letters: ")
    upper_case = 0
    lower_case = 0
    for i in x:
        if i.isupper():
            upper_case += 1
        elif i.islower():
            lower_case += 1
    print "Upercase "+str(upper_case)
    print "Lowecase "+str(lower_case)
#find_uppercase()

def digit_sum_from_letters(x):
    a = int("%s" % x)
    b = int("%s%s" % (x,x))
    c = int("%s%s%s" % (x,x,x))
    d = int("%s%s%s%s" % (x,x,x,x))
    return a+b+c+d
#print digit_sum_from_letters(4) 

#or
def digit_sum(x):
    sequence = [str(x)*i for i in range(1,x+1)]
    sequence = map(int,sequence)
    print sum(sequence)
#digit_sum(4)

def remove_odd_numbers():
    x = raw_input("Numbers comma separated: ")
    x = x.split(",")
    new_list = []
    for i in x:
        if int(i) % 2 != 0:
            new_list.append(i)
    print ",".join(new_list)
#remove_odd_numbers()	

def bank():
    my_dict = {}
    i = 1
    while True:
        x = raw_input("Letter space amount: ")
        if x:
            x = x.split(" ")
            my_dict.update({x[0]+str(i):x[1]})
            i += 1
        else:
            break
    #deposit = {k:v for (k,v) in my_dict.items() if k is "D"}
    deposit = [int(v) for (k,v) in my_dict.items() if "D" in k]
    withdrawl = [int(v) for (k,v) in my_dict.items() if "W" in k]

    print sum(deposit) - sum(withdrawl)
#bank()

import re
def check_passwords():
    x = raw_input("Comma separated passwords: ")
    x = x.split(",")
    special_characters = re.compile("/$|@|#")
    accepted_passwords = []
    for i in x:
        if any(number.isdigit() for number in i) and any(letter.isalpha() for letter in i) and re.search(special_characters, i) and len(i) > 6 and len(i) < 13 and re.search("[A-Z]",i):
            accepted_passwords.append(i)
    print ",".join(accepted_passwords)
#check_passwords()

#print set(raw_input().split(","))

#build a game

def build_board(board):
    for line in board:
        for item in line:
            print item,
        print

def game():
    from random import randint
    your_ship = raw_input("First define your ship: ")
    computer_ship = str(randint(0,4))+str(randint(0,4))
    computer_board = [["(O)" for x in range(0,5)] for x in range(0,5)]
    my_board = [["(O)" for x in range(0,5)] for x in range(0,5)]
    turns = 0
    computer_turn = 0
    human_turn = 1
    computer_choice_history = []
    while(True):
        if human_turn:
            human_turn = 0
            computer_turn = 1
            x = raw_input("Your turn now, row,column: ")
            row = int(x[0])
            column = int(x[2])
            if row > 4 or row < 0 or column > 4 or column < 0:
                print "Not even on the map. Try again"
                human_turn = 1
                computer_turn = 0
                continue
            elif computer_board[row][column] == "(X)":
                human_turn = 1
                computer_turn = 0
                print "You aimed that already."
                continue
            if (row == int(computer_ship[0]) and column == int(computer_ship[1])):
                print "Congratulation, you won"
                break
            else:
                computer_board[row][column] = "(X)"
                build_board(computer_board)
        if computer_turn:
            computer_choice = str(randint(0,4))+str(randint(0,4))
            while(True):
                if computer_choice not in computer_choice_history:
                    break
                else:
                    computer_choice = str(randint(0,4))+str(randint(0,4))
            computer_choice_history.append(computer_choice)
            print "Computer choice is "+computer_choice
            if computer_choice[0] == your_ship[0] and computer_choice[1] == your_ship[2]:
                print "computer has won. Loser!"
                break
            else:
                my_board[row][column] = "(X)"
                build_board(my_board)
            human_turn = 1
            computer_turn = 0
#game()

#www. hackerrank. com/challenges/no-idea
def calculate_happiness():
    happiness = 0
    integer_lengths = raw_input();
    n = raw_input();
    n = n.split(" ")
    m_a = raw_input();
    m_a = m_a.split(" ")
    m_b = raw_input();
    m_b = m_b.split(" ")

    for i in n:
        if i in m_a:
            happiness += 1
        if i in m_b:
            happiness -= 1
    print happiness
#calculate_happiness()

#or
def calculate_happiness2():
    import fileinput
    x = 0
    happiness = 0
    for line in fileinput.input():
        x += 1
        line = line.rstrip("\n\r")
        if x == 2:
            n = line.split(" ")
        if x == 3:
            m_a = line.split(" ")
        if x == 4:
            m_b = line.split(" ")
    for i in n:
        if i in m_a:
            happiness += 1
        if i in m_b:
            happiness -= 1
    print(happiness)
#calculate_happiness2()

def student_average():
    import fileinput
    x = 1
    students = []
    student_dict = {}
    for line in fileinput.input():
        if x == 1:
            student_number = line
        else:
            students.append(line)
        x += 1
    called_student = students[len(students)-1]
    del students[len(students)-1]
    subjects = ["Maths", "Physics", "Chemistry"]
    for i in students:
        i = i.rstrip("\n")
        values = i.split(" ")
        grades = [values[1],values[2],values[3]]
        student_dict[values[0]] = dict(zip(subjects,grades))
    sum = 0
    for grade in student_dict[called_student].values():
        if(float(grade)):
            sum += float(grade)
    print("%.2f" % round(sum / len(subjects), 2))
#student_average()

'''
ways to grab the input:
l = []
while True:
    s = raw_input()
    if s:
        lines.append(s)
    if not s:
        break
        
or if we know the lines from first input:
n=int(raw_input())
for i in range(n):
    line=raw_input().split()
'''

def multisort():
    from operator import itemgetter
    x = ["Tom,19,80","John,20,90","Jony,17,91","Jony,17,93","Json,21,85"]
    print sorted(x,key = itemgetter(0,1,2))
#multisort()

class GeneratorNumbersDivisible(object):

    def __init__(self,n,division):
        self.n = n
        self.division = division
        for i in self.divisible():
            print i

    def divisible(self):
        numbers = []
        for i in range(0,self.n):
            if i % self.division == 0:
                yield i

#generator = GeneratorNumbersDivisible(342,7)

class robotMovements(object):

    def __init__(self):
        self.movelist = self.registerMovements()
        print self.processMovements()

    def registerMovements(self):
        movements = []
        while True:
            x = raw_input()
            if x:
                movements.append(x)
            if not x:
                break
        return movements

    def processMovements(self):
        x_way = 0
        y_way = 0
        for i in self.movelist:
            i = i.split(" ")
            i[1] = float(i[1])
            i[1] = int(round(i[1]))
            if i[0] == "UP":
                x_way += i[1]
            elif i[0] == "DOWN":
                x_way -= i[1]
            elif i[0] == "RIGHT":
                y_way += i[1]
            elif i[0] == "LEFT":
                y_way -= i[1]
        return abs(x_way) + abs(y_way)
#robotMovements()

def combine_2_lists():
    a = [1,1,1,2,2,2,3,3,3,3]
    b = ["Sun", "is", "bright", "June","and" ,"July", "Sara", "goes", "to", "school"]
    c = []
    for i in range(len(a)):
        if len(c)<a[i]:
            c.append(b[i])
        else:
            c[a[i]-1] += " " + b[i]
    return c
#print(combine_2_lists())

def sortDictionary():
    inputDictionary = {
        "John" : {
            "DOB" : 1990,
            "DOD" : 1995
        },
        "Bob" : {
            "DOB": 1993,
            "DOD": 1997
        },
        "Elton" : {
            "DOB": 1995,
            "DOD": 1996
        },
        "Romney" : {
            "DOB": 1995,
            "DOD": 1996
        },
        "Mitt" : {
            "DOB": 1995,
            "DOD": 2000
        },
        "Barack" : {
            "DOB": 1996,
            "DOD": 2001
        },
        "Claudiu" : {
            "DOB": 1996,
            "DOD": 2005
        }
    }
    return inputDictionary
    return sorted(inputDictionary.items(), key=lambda (x,y): y["DOD"])

def highPopulation(dict):
    years = {}
    for x in dict:
        personYears = range(dict[x]["DOB"],dict[x]["DOD"] + 1)
        for y in personYears:
            if y in years:
                years[y] += 1
            else:
                years[y] = 1
    return sorted(years.items(), key = lambda x : x[1], reverse = True)
#print(highPopulation(sortDictionary()))

def highPopulation2(dict):
    new_dict = {}
    for x in dict:
        dataBirth = dict[x]["DOB"]
        if dataBirth not in new_dict:
            new_dict[dataBirth] = 1
        else:
            new_dict[dataBirth] += 1
        dateDeath = dict[x]["DOD"] + 1
        if dateDeath not in new_dict:
            new_dict[dateDeath] = -1
        else:
            new_dict[dateDeath] -= 1
    sortedList = sorted(new_dict.items(), key = lambda x : x[0])
    population = 0
    maxYear = [0,0]
    for x in sortedList:
        population += x[1]
        if population > maxYear[1]:
            maxYear[0] = x[0]
            maxYear[1] = population
    return maxYear
#print(highPopulation2(sortDictionary()))

def binarySearch(sequence, value):
    lo = 0
    hi = len(sequence) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sequence[mid] < value:
            lo = mid + 1 # the new low is half
        elif value < sequence[mid]:
            hi = mid - 1 # the new high is half
        else:
            return mid
    return "Element not in list"
#print(binarySearch([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],67))

def numSetBits(A):
    bitNumber = bin(A)
    numberOfOnes = 0
    for x in str(bitNumber):
        if x == "1":
            numberOfOnes += 1
    return numberOfOnes
#print(numSetBits(11))

class Solution:
    # @param a : list of integers
    # @param b : integer
    # @return a list of integers
    def rotateArray(self, a, b):
        ret = []
        a = a.split(" ")
        for i in xrange(len(a)):
            ret.append(a[(i + b) % len(a)])
        return ret
o = Solution()
#print(o.rotateArray("19 14 5 14 34 42 63 17 25 39 61 97 55 33 96 62 32 98 77 35", 56))

# https://www.careercup.com/question?id=5765581773996032
# convert a number to english words
def convertNumberToEnglish(number):
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifthteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    powers = [("hundred",100), ("thousand",1000), ("million",1000000), ("billion",1000000000), ("trillion",1000000000000)]

    if number < 10:
        return ones[number]
    elif 10 <= number < 20:
        return teens[number % 10]
    elif 20 <= number < 100:
        if ones[number % 10] is not "zero":
            return tens[number // 10 - 1]+" "+ones[number % 10]
        else:
            return tens[number // 10 - 1]
    else:
        finalNumber = []
        for word, integer in reversed(powers):
            if number // integer:
                finalNumber.append(convertNumberToEnglish(number // integer)+" "+word)
                if convertNumberToEnglish(number % integer) is not "zero":
                    finalNumber.append(convertNumberToEnglish(number % integer))
                return " ".join(finalNumber)
#print(convertNumberToEnglish(1076101))

# https://www.careercup.com/question?id=5726440612954112
# sliding window algo
# Given an array of positive integers and a target total of X, find if there exists a contiguous subarray with sum = X
def contiguousSubarray(myList, mySum, window = 1):
    if window <= len(myList):
        for index,item in enumerate(myList):
            currentWindow = myList[index:index+window]
            if sum(currentWindow) == mySum:
                return currentWindow # True
        else:
            return contiguousSubarray(myList, mySum, window + 1)
    return False

print(contiguousSubarray([1,3,5,18],26))

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a
print(gcd(8,20))


# https://leetcode.com/problems/regular-expression-matching/
def isMatch(myString,pattern):
    if len(myString):
        if not len(pattern):
            return False
        isDot = pattern[0] == "."
        isStar = False
        if (len(pattern) > 1):
            isStar = pattern[1] == "*"
        if isStar:
            if isDot:
                if len(pattern) == 2:
                    return True # .* matches everything
                else:
                    return isMatch(myString, pattern[2:])
            for index,item in enumerate(myString): # aaaaab a*b is True
                if pattern[0] is not item:
                    return isMatch(myString[index:], pattern[2:])
            if len(pattern) > 2:
                return isMatch(myString[2:], pattern[2:])
            else:
                return True
        elif myString[0] == pattern[0]:
            return isMatch(myString[1:],pattern[1:])
        elif isDot:
            return isMatch(myString[1:],pattern[1:])
        else:
            return False
    if len(pattern):
        return False
    return True
#print(isMatch("aa","a*c*a"))

def weightedMean():
    length = input()
    elements = list(map(int,input().split(" ")))
    weights = list(map(int,input().split(" ")))
    elementsWeights = [x[0]*x[1] for x in zip(elements,weights)]
    return round(sum(elementsWeights) / float(sum(weights)),1)
#print(weightedMean())

def meanMedianMode():
    length = 10
    myList = "64630 11735 14216 99233 14470 4978 73429 38120 51135 67060"
    myList = sorted(map(int, myList.split(" ")))
    mean = sum(myList) / float(length)
    myList.sort()
    if length % 2:
        median = myList[length // 2]
    else:
        median = (myList[length / 2 - 1] + myList[length / 2 ]) / float(2)
    modeList = dict([i, myList.count(i)] for i in myList)
    sortedModeList = sorted(modeList.items(), key=lambda x: x[1], reverse=True)
    heighestMode = sortedModeList[0][1]
    multipleModes = []
    for x in sortedModeList:
        if x[1] == heighestMode:
            multipleModes.append(x[0])
        else:
            break

    mode = min(multipleModes)
    return str(mean) + "\n" + str(median) + "\n" + str(mode)
#print(meanMedianMode())

import statistics as st
def findQuartiles():
    length = int(input())
    myList = list(map(int,input().split(" ")))
    myList.sort()
    q2 = round(st.median(myList))
    middle = length // 2
    q1 = round(st.median(myList[:middle]))
    if length % 2 is not 0:
        q3 = round(st.median(myList[middle + 1:]))
    else:
        q3 = round(st.median(myList[middle:]))
    return str(q1) + "\n" + str(q2) + "\n" + str(q3)
#print(findQuartiles())
