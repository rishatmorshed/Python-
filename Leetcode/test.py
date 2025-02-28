import os
# phone_no = {
#     'Hamim': 123,
#     'Hadi': 234,
#     'Kabbo': 456,
#     'Soddo': 567
# }
# phone_no = student_dictt([('Hamim', 123),('Soddo', 567),('Kabbo', 456,),('Hadi', 234,)])
# phone_no["Morshed"] = {'Home_No':123, 'Office': 121}
# # print(phone_no['Morshed']['Home_No']['Office'])
# print(phone_no.get('morshed'))         
# data = {
#     1:'kabbo',
#     2:'saddo',
#     3:'hamim',
#     0:'hadi'
# }
# student_dict = defaultstudent_dictt(list)
# nums = [1,2,3,4,5,6,7,8,9,10]
# for i in nums:
#     student_dict[i%2].append(i)
# print(student_dict)


# Functions with and without Argument

# def add(*numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum+i
#     print(sum)
# add(5,5,5,5)

# def multiplication(*mul):
#     ans = 1
#     for i in mul:
#         ans = ans*i
#     print(f"Multiplication result: {ans}")



# multiplication(2,3,-6,8)
# multiplication(2,5,8,9,0,6)

#Coding Exercise

# def color(cover, height, width):
#     cans = math.ceil((height*width)/cover)
#     print(f"No of cane required : {cans}")

# h = int(input("Enter the height of the wall in meter:\n"))
# w = int(input("Enter the width of the wall in meter:\n"))
# coverage = int(input("Enter the coverage area:\n"))
# color(width = w, height = h, cover = coverage)
    



# coding Exercise two: Check the number is prime or not

# def is_prime(n):
#     if n>1:
#         for i in range(2, int(n/2)+1):
#             if (n%i == 0):
#                 print("Not a prime number")
#                 break
#         else:
#             print("Prime number")
#     else:
#         print("Not a prime number")

# n= 2
# is_prime(n)

# Coding Exercise

# def grade_cal(mark):
#     student_dict ={}
#     for i in mark: # now here i = jenny
#         marks = mark[i] # mark[jenny] = 92. so 92 will assign into marks variable
#         if marks >= 91 and marks<=100:
#             student_dict[i] = 'A+'
#         elif marks>=81 and marks<=90:
#             student_dict[i] = 'A'
#         elif marks>=71 and marks<=80:
#             student_dict[i] = 'B+'
#         elif marks>=61 and marks<=70:
#             student_dict[i] = 'B'
#         elif marks>=51 and marks<=60:
#             student_dict[i] = 'C'
#         elif marks>=41 and marks<=50:
#             student_dict[i] = 'D'
#         elif marks< 40:
#             student_dict[i] = "F"
#     print(student_dict)


# def mark_to_grade(sheet):
#     new_dic = {}
#     for i in sheet:
#         if i not in sheet:
#             marks = new_dic[i]
#             if marks>91 and marks<100:
#                 new_dic[i] = 'A+'
#     print(new_dic)

#1) ######################################### Student Grade sheet using dictionary
# def mark_to_grade(old_dic):
#     new_dict = {}
#     for i in old_dic:
#         mark = old_dic[i]
#         if mark>=91:
#             new_dict[i] = "A+"
#         elif mark>=81:
#             new_dict[i] = "A"
#         elif mark>=71:
#             new_dict[i] = "B+"
#         elif mark>=61:
#             new_dict[i] = "B"
#         elif mark>=51:
#             new_dict[i] = "C"
#         elif mark>=41:
#             new_dict[i] = "D"
#         elif mark<40:
#             print("Fail")
#     print(new_dict)


# st_marks = {
#     "Jenny" : 92,
#     "Harry": 78,
#     "Dimpy": 56, 
#     "Rahul": 41, 
#     "Ankit": 99, 
#     "Prem": 34
# }
# mark_to_grade(st_marks)



#2) ####################################(How to add a new dictionary in a list using function )
# student_data = [
#     {
#         'Name': 'Mahbub',
#         "Roll": 2114,
#         'Age': 24,
#         "Course": 'python' 
#     },
#     {
#         'Name': 'Morshed',
#         "Roll": 2115,
#         'Age': 25,
#         "Course": 'Java' 
#     }
# ]
# print(student_data)

# def add_new_student(name, roll_no, st_age, course_name):
#     new_student = {}
#     new_student['Name'] = name
#     new_student['Roll'] = roll_no
#     new_student['Age'] = st_age
#     new_student['Course'] = course_name
#     student_data.append(new_student)
#     print(student_data)

# add_new_student("Rishat", 30, 23, "C++")


#3) ##################################### Check Leap Year or Not!
# def check_leepYear(year):
#     if (year % 4 == 0):
#         if (year % 100 == 0):
#             if (year % 400 == 0):
#                 print(f" {year} is a leap year")
#             else:
#                 print(f"{year} is not a leap year")
#         else:
#             print(f"{year} is a leap year")
#     else:
#         print(f"{year} is not a leap year")

# want_to_continue = True
# while want_to_continue:
#     year = int(input("Which year you want to check?\n"))
#     check_leepYear(year)
#     print("Do you want to check again:?")
#     get_ans = input()
#     if get_ans == 'no':
#         want_to_continue = False



#4) ################################### (How many days in a month)
# def check_leapYear(year):
#     if (year % 4 == 0):
#         if (year % 100 == 0):
#             if (year % 400 == 0):
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# def No_Of_Days(year, m_name):
#     days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     is_leap = check_leapYear(year)
#     if is_leap == True and m_name == 2:
#         return 29
#     else:
#         return days_list[m_name-1]


# year_name = int(input("Enter  a year:"))
# m_name = int(input("Enter a month:"))
# days = No_Of_Days(year_name, m_name)
# print(days)

#5)  #############################################{Return and Printing}
# def func2(x):
#     return x*5

# def func1(a, b):
#     ans = a+b
#     print(ans)
#     x = func2(ans)
#     print(x)
# func1(2,5)


#6)  #############################################(Recursion in python)

# def countdown(n):
#     if n == 0:
#         print("Done")
#         return
#     else:
#         print(f"value of n: {n}")
#         countdown(n-1)   #Recursive call with a value which is decreasing


# n = int(input("Enter a number: "))
# countdown(n)

#7)  #######################################{ Simple Calculator Project}

# def calculation(first_no, next_no, sign):
#     if sign == '+':
#         result = first_no + next_no
#     elif sign == '-':
#         result = first_no - next_no
#     elif sign == '*':
#         result = first_no * next_no
#     elif sign == '/':
#         result = first_no / next_no
#     print(f"{first_no} {sign} {next_no} =",result)
#     further_input=input(f"Enter 'y' to continue calculation with {result} or 'n' to start new calculation or 'x' to exit:\n")
#     next_chioce=input()
#     further_opinion(next_chioce, result) 

# def further_opinion(next_chioce, first_result):
#     if next_chioce == 'y':
#         sign =(input("Pick an operator: "))
#         nxt_num = int(input("Enter next number: "))
#         calculation(first_result, nxt_num, sign)
#     elif next_chioce == 'n':
#         func_1()
#     elif next_chioce == 'x':
#         exit
#         print("Have a nice day! bye...")


# def func_1():
#     first_no = int(input("Enter first number: "))
#     print('+', '-', '*', '/')
#     operator = input("Pick an operation: ")
#     next_no = int(input("Enter next number: "))
#     calculation(first_no, next_no, operator)
# func_1()

#8)  ##################################################{Simple Calculator using Recursion}

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b

# operations_dict={
#     '+' : add,
#     '-' : sub,
#     '*' : mul,
#     '/' : div
# }
# def M_calculator():
#     number1 = float(input("Enter first number: "))
#     for symbol in operations_dict:
#         print(symbol)
#     continue_flag = True
#     while continue_flag:        
#         op_symbol = input("Pick an operator: ")
#         number2 = float(input("Enter next number: "))
#         calculator_function = operations_dict[op_symbol]  # dictionary values stored in here
#         output = calculator_function(number1, number2)
#         print(f"{number1} {op_symbol} {number2} = {output}")
#         should_continue=input(f"Enter 'y' to continue calculation with {output} or 'n' to start a new calculation or 'x' to exit: ").lower()
#         if should_continue == 'y':
#             number1 = output
#         elif should_continue == 'n':
#             continue_flag = False
#             os.system('cls') #This will clear previous output in cosole screen 
#             M_calculator()   # Recursion call
#         elif should_continue == 'x':
#             continue_flag = False
#             print("Bye")
# M_calculator()

#9)  ################################################ { Local and Global Scope}
# a = 15   #Global 
# def display():
#     a = 10     # local 
#     def show():
#         print("inside",a)
#     show()      # We have to call it inside display function.
#                 # bcz show() function defined inside display function
# display()
# print("Outside",a)

# #Example for block scope 
# a, b = 10, 5
# if a>b:         
#     c = a+b   # consider as a global. bcz there is no functions
# print(c)   # it'll print bcz in python there is no block scope 


#10) #####################################################{What is Global Keyward}
#a = 10
# def display():
#     a = 20
#     def show():
#         global a
#         a = 30
#     print(f"Value of a before calling show() function is {a}")  #here a = 20
#     show()
#     print(f"Value of a after calling show() function is {a}")   #here a = 20
# display()
# print(a)    #here a = 30. bcz show() create a global variable a and assign a = 30

######################## global keyword is used to modifie value within a function 
# name = 'Mahbub'
# def p_name():
#     global name
#     name = name + ' Morshed'
# print(name)
# p_name()
# print(name)

#11) Project ##############################{Number Guessing}
# import random
# def easy_type(rand_no):
#     no_of_attempt = 10
#     while no_of_attempt>=1:
#         print(f"You have {no_of_attempt} attemps remaining to guess the number!")
#         no_of_attempt -= 1
#         guess_no = int(input("Make a guess: "))
#         if rand_number < guess_no:
#             print("Your guess is too high.")
#             if rand_number != guess_no and no_of_attempt>=1:
#                 print("Guess again")
#         elif rand_number > guess_no:
#             print("Your guess is too low.")
#             if rand_number != guess_no and no_of_attempt>=1:
#                 print("Guess again")
#         elif rand_number == guess_no:
#             print(f"Your guess was right...The answer is {guess_no}")
#             break
#     if no_of_attempt<1:
#         print("You have no more attempts left. You lose...")

# def hard_type(rand_no):
#     no_of_attempt = 5
#     while no_of_attempt>=1:
#         print(f"You have {no_of_attempt} attemps remaining to guess the number!")
#         no_of_attempt -= 1
#         guess_no = int(input("Make a guess: "))
#         if rand_number < guess_no:
#             print("Your guess is too high.")
#             if rand_number != guess_no and no_of_attempt>=1:
#                 print("Guess again")
#         elif rand_number > guess_no:
#             print("Your guess is too low.")
#             if rand_number != guess_no and no_of_attempt>=1:
#                 print("Guess again")
#         elif rand_number == guess_no:
#             print(f"Your guess was right...The answer is {guess_no}")
#             break
#     if no_of_attempt<1:
#         print("You have no more attempts left. You lose...")

# print("Let me think of a number between 1 to 50.")
# rand_number = random.randint(1, 50)
# game_type = input("Choose level of difficulty...Type 'easy' or 'hard': ").lower()
# if game_type == 'easy':
#     easy_type(rand_number)
# elif game_type == 'hard':
#     hard_type(rand_number)

#11) Project ##############################{Number Guessing 2nd Method}

# import random

# EASY_LEVEL_ATTEMPTS = 10
# HARD_LEVEL_ATTEMPTS = 5
# def set_difficulty(level_type):
#     if level_type == 'easy':
#         return EASY_LEVEL_ATTEMPTS
#     elif level_type == 'hard':
#         return HARD_LEVEL_ATTEMPTS
    
# def check_answer(guessed_num, answer, attempts):
#     if guessed_num<answer:
#         print("Your guess is too low")
#         return attempts-1
#     elif guessed_num>answer:
#         print("Your guess is too high.")
#         return attempts-1
#     else:
#         print(f"Your guess was right...The answer is {answer}")

# def game():
#     continue_flag = True
#     while continue_flag:
#         print("Let me think of a number between 1 to 50.")
#         answer = random.randint(1, 50)
#         level = input("Choose level of difficulty...Type 'easy' or 'hard': ").lower()
#         attempts = set_difficulty(level)
#         guessed_num = 0
#         while guessed_num != answer:
#             print(f"You have {attempts} attemps remaining to guess the number!")
#             guessed_num = int(input("Guess a number: "))
#             attempts = check_answer(guessed_num, answer, attempts)
#             if attempts == 0:
#                 print(f"You are out of guesses...You lose! The answer was {answer}")
#                 re_play=input("Press 'y' to play again or 'x' to exit: ")
#                 if re_play == 'y':
#                     game()
#                 elif re_play == 'x':
#                     continue_flag = False
#                     print("Bye.. Have a good day!")
#                 return 
#             elif guessed_num != answer:
#                 print("Guess again")
# game()