''' Assignment for the course "Advanced Programming with python",
    Python program for set of problems/questions. '''
'''All the methods are numbered with the question number in comment following the codes, defined inside one class called "Assignmnet".
    Use the separate test.py fle to see/check each methods output,by creating an instance of the class - object.'''

class Assignment:
#1 cubic method
    def cube(num):
        input_num = int(input("Insert the number: "))
        cubic = num ** 3
        print(f"The cube of {input_num} is {cubic}.")

#2 area of triangle
    def triangle(self,height,width):
        Area = 1/2*height*width
        return Area

#3 area of rectangle
    def rectangle(self,length,width):
        Area = length*width
        return Area

#4 linear equation y = mx+b
    def Line(self,m , b, x):
        y = m*x + b
        return y

#5 intersected or parallel lines to each other
    def Intersect(self,m1,b1,m2,b2):
        if m1 == m2:
            return 1  #teh lines are intersecting.
        else:
            return 0

#6 factorial of posetive integer
    def factorial(self,num):
        if num == 1 or num == 0:
            return 1
        else:
            return num * self.factorial(num - 1)  #at iteration of 1, the function return this return before returnning the second from above.
    def fact_test(self):
        num = int(input("Insert a positive number"))
        if num < 0:
            print("Insert a posetive # please!")
        else:
            print(f"The factorial of {num} is {self.factorial(num)}")

#7). Method to display the Fibonacci sequence
    def recur_fibo(self):
        num = int(input("Insert the number to to do the fibonacci sequence: "))
        if num <= 0:
            print("Plese enter a positive integer")
        else:
            print("Fibonacci sequence->:")
            for i in range(num):
                print(self.rec_main(i))

    def rec_main(self,n):
        if n <= 1:
            return n
        else:
            return (self.rec_main(n - 1) + self.rec_main(n - 2))

#8 checking a number either it is prime and doing its digit sum.
    def primeSum(self, num):
    #Checking num is either prime or not
        if num % 2 == 0:
            print(f"{num} is not prime number.")
        else:
            print(f"{num} is prime number.")
    #to do sum of digits
        sum = 0
        for i in str(num):
            sum = sum + int(i)
        print(f"sum of digit is {sum}.")

#9 ordering list of numbers in ascending order.
    def ascending(self):
        arr = [8,2,7,9,1,3]   #sample set of numbers inside an array named arr.
        for i in range(0, len(arr)):
            for j in range(i + 1, len(arr)):
                if (arr[i] > arr[j]):  #swap teh values if arr[i] > arr[j]
                    temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;

        print("Elements of array sorted in ascending order is: ")   #print a return a sorted element, why?
        for i in range(0, len(arr)):
            print(arr[i], end=" ");

#10 list of students with their mark
    def markList(self):
        a = []
        num = int(input("Insert number of students"))
        for i in range(0,num,1):
            a.append(int(input(f"insert mark of {i+1}th student:")))
        maxi = max(a)
        print(f"The maximum score is {maxi}.")

#11 checking a mobile number is valid or not.
    def mobile(self,mob):
        if len(str(mob)) == 9:
            if int(str(mob)[0]) == 9:
                print(f"{mob} is mobile."+str(mob)[0])
            else:
                print(f"{mob} is fixed phone."+str(mob)[0])
        else:
            print("Wrong digits length!")

#12 finding maximum and minimum from a list of numbers.
    def minMax(self):
        a = []
        num = int(input("Insert number of list elements: "))
        for i in range(0,num,1):
            a.append(int(input(f"insert the {i+1}th element of the list:")))
        maxi = max(a)
        mini = min(a)
        print(f"In the list,the maximum is {maxi} and the minimum is {mini}.")

#13 reversing a given number's gigits.
    def reverse(self):
        num = int(input("Enter an integer number: "))
        revs_number = 0
        while (num > 0):
            # Logic
            remainder = num % 10
            revs_number = (revs_number * 10) + remainder
            num = num // 10
        print("The reversed number is : {}".format(revs_number))

#14 finding greatest common divisor of two mumbers.
    def GCD(self,num1,num2):
        divisors = "123456789"
        element = ""
        if num1 > num2 and num1 % num2 ==0:
            gcd = num2
        elif num2 > num1 and num2 % num1 == 0:
            gcd = num1
        else:
            for i in divisors:
                a = num1 % int(i)
                b = num2 % int(i)
                if a == 0 and b == 0:
                    element += i
            gcd = max(element)
        return gcd

#15 finding least common multiple of two numbers.
    def LCM(self,num1,num2):
        if num1 > num2 and num1 % num2 == 0:
            lcm = num1
        elif num2 > num1 and num2 % num1 == 0:
            lcm = num2
        else:
            lcm = num1*num2
        return lcm

#16 doing sum of the given arthimetic sequence.
    #By using the arthimetic series, I know as 97/99 is the 49th element in the sum.
    def sum(self):
        num = 1
        den = 3
        sum = num/den
        count = 1
        for i in range(48):
            count+=1
            num = den
            den = num + 2
            sum += num/den
        return sum, count

#17 calculating the 10th digit in ISBN, provide the first 9 digits are given.
    def ISBN(self):
        # here I consider as the user need enter only the 9 digit length ISBN
        input_isbn = int(input("Enter The nine digits of your ISBN"))
        isbn = str(input_isbn)
        if len(isbn) == 8:
            new_isbn = '0'
            new_isbn +=isbn
            isbn = new_isbn
        j = 1
        sum = 0
        for i in range(9):
            sum += int(isbn[j-1])*j
            j+=1
            if j == 10:
                break
        check_sum = str(sum%11)
        if check_sum == '10':
             check_sum = 'X'
        ISBN = isbn + check_sum
        print(f"The ISBN for the give nigne digit {isbn} is {ISBN}.")

#18 doing exponential of numbers(e**x) from the euler's equivalent formula given.
    def exp(self):
        n = 15
        x = 1.0
        self.exp_main(x,n)

    def exp_main(self,x,n):
        sum = 1.0
        for i in range(1, n + 1, 1):
            sum += (x ** i) / self.factorial(i)
        print(f"e^{x} =", sum)

#19 finding leap years
    def leapYear(self):
        start_year = 2001
        end_year = 2100
        count = 0
        if start_year < end_year:
            print("List of leap years between " + str(start_year) + " and " + str(end_year) + ":")
        for i in range(start_year, end_year + 1, 1):
            if start_year % 400 == 0 or (start_year % 4 == 0 and start_year % 100 != 0):
                print(start_year,end =" ")
                count = count + 1
                if count % 10 == 0:
                    print()
            start_year += 1
        print("Total number of leap year : ", count)

#20 returning the maximum number from a a given list of numbers with its occurence.
    def numCount(self):
        num = int(input("Enter your list size: "))
        arr =[]
        for i in range(0,num,1):
            arr.append(int(input(f"Enter the {i+1}th integer : ")))
        max = arr[0]
        count = 1
        for i in range(0, len(arr)):
            if (arr[i] > max):  # swap the values if arr[i] > arr[j]
                max = arr[i];
                count =1
            elif arr[i]==max:
                count+=1
        print(f"The largest number is {max} \n The occurence is {count} times.")

#21 finding numbers where there digits cube sum equal to the number itself, between 100 and 1000.
    def intBtw(self):
        store = []
        for xyz in range(101,1000,1): # list num between 101 and 1000,execluding the higher index, increment with 1
            num = str(xyz)
            cube_sum = int(num[0])**3 +int(num[1])**3+ int(num[2])**3
            print(xyz)
            if xyz == cube_sum:
                store.append(xyz)
        print(f"The numbers where their digits cube sum equal to the number itself are: {store}.")

#22 number of digits an entered number have.
    def digitCount(self):
        print("This program will give the # of digits it has.")
        while(True):
            num = int(input("Enter the number: "))
            s_num = str(num)
            digit = len(s_num)
            if num < 0 :
                print("Bad argument,terminated!")
                break
            else:
                print(f"{num} has {digit} digits.")

#23 counting number of prime numbers between 2 and an entered number N.
    def primeCount(self):
        N = int(input("please Insert your N: "))
        count = 0
        for num in range(2, N+1, 1):
            f = 0
            for i in range(1,num+1,1):
                if num % i == 0:
                    f+= 1
            if f == 2 :  #number having factor only 1 and itself is a prime number.
                count+=1
        print(f"There are {count} prime numbers between 2 and {N}.")

#24 Identifying perfect numbers in the range of an entered number num.
    def perfectNum(self):
        num = int(input("Enter the number"))
        sum = 0
        divisor = []
        for i in range(1,num,1):
            if num%i == 0:
                sum +=i
                divisor.append(i)
        if num == sum:
            print(f"{num} is perfect number.\n It's proper divisor are {divisor}.")
        else:
            print(f"{num} is not perfect number.")

#25 doing the sum and average of posetive and negative numbers, out of an entered set of numbers.
    def posNegAve(self):
        i = 1       # intialize the index
        countPos = 0
        countNeg = 0
        sum = 0
        while (i != 0):
            if (i > 0):
                countPos += 1
            elif (i < 0):
                countNeg += 1
            i = int(input("Enter an interger: "))
            sum += i
        count = (countPos-1) + countNeg
        average = sum / count
        print("The number of positive numbers =", countPos-1)
        print("The number of negative numbers =", countNeg)
        print("The sum is =", sum)
        print("The average is =", float(average))

#26 calculating tution cost
    def tutionCost(self):
        totalCost = 0
        tuition = 10000
        for year in range(1, 15):
            # if year<11:
            print(f"Tution in the {year}th year is : $", tuition)
            if year>10:
                totalCost += tuition

            tuition += tuition * 0.05
        print("Total cost for four years', tuition after ten years is : $", totalCost)

#27 unit converter
    def converter(self):
        print("+ Unit Conversion + \n\t1. Kilograms to pounds.\n\t2. Miles to Kilometers.\n\t3. Hours to minutes.\n\t Q or q Quite:  ")
        choice = int(input("Enter your choice! "))
        while(True):
            if choice == 1:
                kg = int(input("Enter the kilograms: "))
                pound = kg*2.204623
                print(f"{kg}Kg is equal to {pound}lbs.")
            elif choice == 2:
                ml = int(input("Enter the Miles: "))
                kilometer = ml * 1.609344
                print(f"{ml}mile is equal to {kilometer}Km.")
            elif choice == 3:
                hr = int(input("Enter the hours: "))
                minutes = hr * 60
                print(f"{hr}hrs is equal to {minutes}s.")
            elif choice =="Q" or choice == 'q':
                break
#28 finding the first and the second maximum mark from list of student
    def studScore(self):
        a = {}
        num = int(input("Insert number of students"))
        for i in range(0, num, 1):
            name =  input(f"Enter {i+1}th Student's name:")
            mark = int(input(f"insert mark of {name}:"))
            a[name] = mark
        stu_max = max(a)
        max_value = a[stu_max]  #store before it is deleted , when assign to a variable it references to the same address.
        del a[stu_max]
        stu2_max = max(a)
        print(f"The top-maximum score is {max_value} --- Scored by {stu_max}")
        print(f"The second-maximum score is {a[stu2_max]} --- Scored by {stu2_max}")

#29 finding the maximum score from list of student's score
    def highestScor(self):
        a = {}
        num = int(input("Insert number of students"))
        for i in range(0, num, 1):
            name = input(f"Enter {i + 1}th Student's name:")
            mark = int(input(f"insert mark of {name}:"))
            a[name] = mark
        stu_max = max(a)
        print(f"The maximum score is {a[stu_max]} --- Scored by {stu_max}")

#30 number those are divisible by 5 and 6, but not both between 100 and 200.
    def numBtn(self):
        count = 0
        for i in range(100,200,1):
            if i%5 == 0:
                print(i,end = " ")
                count+=1
                if count % 10 == 0:
                    print()
            elif i%6 == 0:
                print(i,end = " ")
                count+=1
                if count % 10 == 0:
                    print()

#31  ASCII between ! and ~
    def ascii(self):
        count = 0
        print("Lists of ASCII character between ! and ~ :")
        for i in range(33, 127):    #ASCII of ! = 33 and ASCII OF ~ = 126
            print(chr(i),end = " ")
            count += 1
            if count % 10 == 0:
                print()

#32 program to generate patterns.
    def pattern1(self):
        for i in range(1,7):
            for k in range(1, 7-i):
                print(" ", end=" ")
            for j in range(i,0,-1):
                print(j,end=" ")
            print()

    def pattern2(self):
        for i in range(1,7):
            for k in range(1, 7-i+1):
                print(k, end=" ")
            print()
            for j in range(0,i,1):
                print(" ",end=" ")

    def pattern3(self):
        for i in range(1,7):
            for k in range(1, 7-i+1):
                print(k, end=" ")
            for j in range(1,i,1):
                print(" ",end=" ")
            print()

    def pattern4(self):
        for i in range(1, 7):
            for k in range(1, i+1):
                print(k, end=" ")
            for j in range(1, 7-i+1, 1):
                print(" ", end=" ")
            print()

#33 pyramid pattern generator for an entered number of rows.
    def patternPyramid(self):
        n = int(input("Enter an integer,between 1 and 15:  "))
        for i in range(1,n+1):
            for k in range (1,n-i+1):
                print(" ",end=" ")
            for j in range(i,0,-1):
                print(j,end=" ")
            for m in range(2,i+1):
                print(m,end=" ")
            print()

#34 exponential(base 2) pattern.
    def patternExp(self):
            n = 8
            for i in range(1,n+1):
                for k in range (1,n-i+1):
                    print(" ",end=" ")
                for j in range(0,i,1):
                    print(2**j,end=" ")
                for m in range(i-2,-1,-1):
                    print(2**m,end=" ")
                print()

#35 loan amount calculator
    def loanAmount(self):
        loanAmount = int(input("Enter loan amount: "))
        numOfYears = int(input("Enter number of years: "))
        anuIntRate = 5.0
        print("Interest Rate \tMonthly Payment\t\t  Total Payment")
        while (anuIntRate <= 8.0):
            monIntRate = (anuIntRate/1200.0)
            monthlyPayment = (loanAmount*monIntRate)/ ((((1+monIntRate)**(numOfYears*12))-1)/((1+monIntRate)**(numOfYears*12))) * 10 #/((1+monIntRate)**(numOfYears*12))
            totalPayment = (monthlyPayment * numOfYears * 12.0)
            print(anuIntRate, end="%")
            print("\t\t",monthlyPayment,end = " ")
            print("\t\t", totalPayment)
            anuIntRate = anuIntRate + 0.125

#36 decial to hexadecimal converter
    def decToHex(self):
        decimal = int(input("Enter the Decimal number: "))
        a = decimal
        value_pair = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                            5: '5', 6: '6', 7: '7',
                            8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                            13: 'D', 14: 'E', 15: 'F'}
        hexadecimal = ''
        while (decimal > 0):
            remainder = decimal % 16
            hexadecimal = value_pair[remainder] + hexadecimal
            decimal = decimal // 16

        print(f"The hexadecimal form of {a} is 0x{hexadecimal}.")

#37 finding euler's constant e, from the eulers series formula given.
    def euler_e(self):
        x = 1   # for x = 1,e^x = 1.
        n= 10  # take it is as you want like 100 or 50
        self.exp_main(x, n)
#38 listing prime numbers in range of an entered number N, inclusive.
    def isPrime(self):
        N = int(input("please Insert your N: "))
        count = 0
        for i in range(1,N+1,1):
            if N % i == 0:
                count+= 1
        if count == 2 :  #number having factor only one and itself is a prime number.
              print(f"{N} is prime number.")
        else:
            print(f"{N} is not prime number.")
#39 determine eeither a number is even or odd.
    def isEven(self):
        N = int(input("please Insert your N: "))
        if N % 2 == 0:
            print(f"{N} is Even number.")
        else:
            print(f"{N} is an Odd number.")

#40 simple calculator which works basic operations.
    def calculator(self):
        def sum(x,y):
            return x + y
        def difference(x,y):
            return x - y
        def product(x,y):
            return x * y
        def qotient(x,y):
            return x / y
        print("Python Based Mini Calculator: \n   ")
        print("1. for Sum", end = " | ")
        print("2.for Difference", end = " | ")
        print("3.for Product", end = " | ")
        print("4.for Qotient", end = " | ")
        print("Q for Quite")
        while True:
            choice = input("Select the number, corresponding to your choice ")
            if choice in ('1', '2', '3', '4'):
                number1 = float(input("Enter first operand: "))
                number2 = float(input("Enter second operand: "))
                if choice == '1':
                   print(number1, "+", number2, "=", sum(number1, number2))
                elif choice == '2':
                   print(number1, "-", number2, "=", difference(number1, number2))
                elif choice == '3':
                   print(number1, "*", number2, "=", product(number1, number2))
                elif choice == '4':
                   print(number1, "/", number2, "=", qotient(number1, number2))
            elif choice == 'Q' or choice == 'q':
                print("Program Terminated!")
                break
            else:
                print("Invalid Input")

#41 sum of a series of n number's factorial, by calling factorial function above.
    def factSum(self):
        n = int(input("Insert values of n:"))
        sum = 0
        sum+=self.factorial(n)
        print(f"Sum is {sum}.")





