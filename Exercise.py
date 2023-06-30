# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 22:39:54 2023

@author: Abel
"""


# ps0
# =============================================================================
# import math
# x = input("Enter number x:")
# y = input("Enter number y:")
# x = int(x)
# y = int(y)
# print("x**y = ",x**y)
# print("log(x) = ",math.log(x,2))
# =============================================================================
# 2.15
# =============================================================================
# name = input("Enter your name:")
# print("Hello",name)
# hours = input("Enter Hours:")
# rate = input("Enter Rate:")
# print('Pay:',float(hours)*float(rate))
# width = 17
# height = 12.0
# print(type(width//2))
# print(type(width/2.0))
# print(type(height/3))
# print(type(1+2*5))
# Celsius = input('Enter a Celsius temperature:')
# print('The temperature is',9.0/5*int(Celsius)+32,'Fahrenheit')
# =============================================================================
# =============================================================================
# x = int(input("please enter 3 number"))
# y = int(input())
# z = int(input())
# answer = min(x, y, z)
# if x%2 != 0:
#  answer = x
# if y%2 != 0 and y > answer:
#  answer = y
# if z%2 != 0 and z > answer:
#  answer = z
# print(answer)
# =============================================================================
# =============================================================================
# num_x = int(input('How many times should I print the letter X? '))
# to_print = ''
# #concatenate X to to_print num_x times
# while (num_x>0):
#     print('X'+to_print)
#     num_x-=1
# print(to_print)
#
# print('Please enter 10 number:')
# integer_a = int(input())
# flag = 0
# if integer_a%2!=0:
#     flag = 1
#     maximun = integer_a
# x = 9
# while (x>0):
#     x-=1
#     integer = int(input())
#     if integer%2!=0 and integer>integer_a:
#         flag = 1
#         maxmium = integer
# if flag == 1:
#     print('the largest odd number that was entered is:',maxmium)
# else:
#     print('No odd number was entered')
# =============================================================================
# =============================================================================
# sum =2
# for i in range(3,999,2):
#     flag = 0
#     primer = i
#     for j in range(2,i):
#         if primer % j == 0:
#             flag = 1
#             break
#     if flag == 0:
#         sum += primer
# print('the sum is',sum)
# =============================================================================
# =============================================================================
# x = int (input ( ' Enter an integer greater than 2: '))
# smallest_divisor = None
# for guess in range(2,x):
# 	if x % guess == 0:
# 		smallest_divisor = guess
# 		break
# if smallest_divisor != None:
# 	print ( 'largest divisor of', x, 'is', x/smallest_divisor)
# else:
# 	print (x, 'is a prime number ')
# =============================================================================
# =============================================================================
# x = int(input('Please enter a integer:'))
# flag =0
# for pwr in range(2,7):
#     for root in range(1,x):
#         if root**pwr == x:
#             print(root,'**',pwr,'=',x)
#             flag = 1
# if flag ==0:
#     print('no root ** pwr = ',x)
# =============================================================================
# =============================================================================
# epsilon = 0.01
# num_guesses,low = 0,0
# x = int(input('Please enter a positive number:'))
# high = max(1,x)
# ans = (high + low)/2
# while abs(ans**2 - x) >=epsilon:
#     print( ' low =', low,'high =', high,'ans =', ans)
#     num_guesses +=1
#     if ans**2 <x:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low)/2
# print( ' number of guesses =', num_guesses)
# print(ans, 'is close to square root of', x)
# num_guesses,high = 0,0
# low = min(-1,-x)
# ans = (high + low)/2
# while abs(ans**2 - x) >=epsilon:
#     print( ' low =', low,'high =', high,'ans =', ans)
#     num_guesses +=1
#     if ans**2 <x:
#         high = ans
#     else:
#         low = ans
#     ans = (high + low)/2
# print( ' number of guesses =', num_guesses)
# print(ans, 'is close to square root of', x)
# =============================================================================
# =============================================================================
# day,month,year = input('enter your birthday in the form mm/dd/yyyy:').split('/')
# print('You were born in the year',year)
# =============================================================================
# PY4E-3.11-1
# =============================================================================
# hours = float(input("Enter Hours:"))
# rate = float(input("Enter Rate:"))
# if hours>40:
#     pay = (hours-40)*1.5*rate+40*rate
#
# else:
#     pay = hours*rate
# print('Pay:',pay)
# =============================================================================
# =============================================================================
# #PY4E-3.11-2
# try:
#     hours = float(input("Enter Hours:"))
#     rate = float(input("Enter Rate:"))
#     pay = hours*rate
#     print('Pay:',pay)
# except:
#     print('Error, please enter numeric input')
# =============================================================================
# PY4E-3.11-3
# =============================================================================
# try:
#     score = float(input('Please enter score between 0.0 and 1.0:'))
#     if score<=1.0 and score>=0.0:
#         if score>=0.9:
#             print('A')
#         elif score>=0.8:
#             print('B')
#         elif score>=0.7:
#             print('C')
#         elif score>=0.6:
#             print('D')
#         else:
#             print('F')
#     else:
#         print('Bad score')
# except:
#     print('Bad score')
# =============================================================================
# =============================================================================
# #PY4E-4.5-1
# import random
# for i in range(10):
#     x = random.random()
#     print(x)
# =============================================================================
# =============================================================================
# #PY4E-4.7-2 and 3
# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()
#
# def print_lyrics():
#     print("I'm a lumberjack, and I'm okay.")
#     print('I sleep all nihjt and I work all day.')
#
# repeat_lyrics()
# =============================================================================
# =============================================================================
# #PY4E-4.14-6
# def computepay(hours,rate):
#     if hours>40:
#         pay = (hours-40)*1.5*rate+40*rate
#
#     else:
#         pay = hours*rate
#     print('Pay:',pay)
# computepay(45,10)
# =============================================================================
# =============================================================================
# # #PY4E-4.14-7
# def computegrade(score):
#     try:
#         score = float(score)
#         if score<=1.0 and score>=0.0:
#             if score>=0.9:
#                 return 'A'
#             elif score>=0.8:
#                 return 'B'
#             elif score>=0.7:
#                 return 'C'
#             elif score>=0.6:
#                 return 'D'
#             else:
#                 return 'F'
#         else:
#             return 'Bad score'
#     except:
#         return 'Bad score'
# score = input('Please enter score between 0.0 and 1.0:')
# print(computegrade(score))
# =============================================================================
# =============================================================================
# # Newton-Raphson for square root
# # Find x such that x**2 - 24 is within epsilon of 0
# k = float(input('Please enter a number:'))
# epsilon = 0.01
# guess = k/2
# guess_number = 1
# while abs(guess**2 - k) >= epsilon:
#     guess_number = guess_number + 1
#     guess = guess - (((guess**2) - k)/(2*guess))
# print('Square root of', k, 'is about', guess, 'guess number:', guess_number)
# =============================================================================
# =============================================================================
# def find_root(x,power,epsilon):
#     #Find interval containing answer
#     if x<0 and power%2 == 0:
#         return None #Negative number has no even-powered roots
#     low = min(-1,x)
#     high = max(-1,x)
#     #Use bisection search
#     ans = (high + low)/2
#     while abs(ans**power - x) >= epsilon:
#         if ans**power < x:
#             low = ans
#         else:
#             high = ans
#         ans = (high + low)/2
#     return ans
# print(find_root(25, 2, 0.001)+find_root(-8, 3, 0.001) + find_root(16, 4, 0.001))
# =============================================================================
# =============================================================================
# def is_in(a,b):
#     if (a in b) or (b in a):
#         return True
#
#     else:
#         return False
#
# is_in('string', 'stri')
# is_in('stri', 'string')
#
# def test_is_in(a_vals,b_vals):
#     for a in a_vals:
#         for b in b_vals:
#             result = is_in(a,b)
#             if result == True:
#                 val = 'Okay'
#             else:
#                 val = 'None'
#             print(f'a = {a}, b = {b}, val = {val}')
#
#
# a_vals = ('string','being', 'love')
# b_vals = ('stri','belong','I love you')
# test_is_in(a_vals, b_vals)
# =============================================================================
# =============================================================================
# def mult(a,b = None):
#     try:
#         if b == None:
#             print(a)
#         else:
#             print(a*b)
#     except:
#         print('Please enter right number')
#
# mult(19)
# mult(8,9)
# mult(None,2)
# mult(2,None)
# =============================================================================
# =============================================================================
# def log(x,base,epsilon):
#     """Assume x and epsilon int or float, base an int,
#     x > 1,epsilon > 0 & power >= 1
#     Return float y such that base**y is within epsilon of x."""
#     if x > 1 and epsilon >0 and base >= 1:
#         # Find lower bound on ans
#         lower_bound = 0
#         while base*lower_bound < x:
#             lower_bound += 1
#         low = lower_bound - 1
#         high = lower_bound + 1
#         # Perform bisection search
#         ans =(high + low)/2
#         while abs(base**ans - x) >= epsilon:
#             if base**ans < x:
#                 low = ans
#             else:
#                 high = ans
#             ans = (high + low)/2
#         print(ans, f'is close to the log base {base} of',x)
#     else:
#         print('Please enter the right number')
#
# help(log)
# log(3,2,0.001)
# log(9,3,0.00001)
# =============================================================================
# =============================================================================
# def find_last(s,sub):
#     """s and sub are non-empty strings
#     Return the index of the last occurrence of sub in s.
#     Return None if sub dose not occur in s"""
#     try:
#         if len(s) != 0 and sub != '' and s.find(sub) != -1:
#             s_reverse = s[::-1]
#             sub_reverse = sub[::-1]
#             # len(s) = len(sub) + s_reverse.find(sub_reverse) + last_order
#             return len(s) - len(sub) - s_reverse.find(sub_reverse)
#         elif s.find(sub) == -1:
#             return None
#     except:
#         print('Please enter the right strings')
# =============================================================================
# =============================================================================
# divide = lambda a,b: a/b if b else None
# print(divide(20,8))
# =============================================================================
# =============================================================================
# # PY4E-5-5.9-1
# total = 0
# count = 0
# while True:
#     try:
#         a = input('Enter a number:')
#         if a == 'done':
#             break
#         total += int(a)
#         count += 1
#     except:
#         print('Invalid input')
#         continue
# print(total,count,total/count)
# =============================================================================
# =============================================================================
# # PY4E-5.9-2
# total = 0
# count = 0
# max_a = -1000
# min_a = 1000
# while True:
#     try:
#         a = input('Enter a number:')
#         if a == 'done':
#             break
#         a = int(a)
#         total += a
#         count += 1
#         if a > max_a:
#             max_a = a
#         if a < min_a:
#             min_a = a
#     except:
#         print('Invalid input')
#         continue
# print(total,count,max_a,min_a)
# =============================================================================
# =============================================================================
# # PY4E-6.3-1
# string = input('Enter a string:')
# i = 1
# while i <= len(string):
#     print(string[-i])
#     i += 1
# =============================================================================
# =============================================================================
# # PY4E-6.3-2
# fruit = input('Enter a string:')
# print(fruit[:])
# =============================================================================
# =============================================================================
# # PY4E-6.4-3
# def count(string, letter):
#     count = 0
#     for a in string:
#         if a == letter:
#             count += 1
#     return count
# print(count('banana','a'))
# =============================================================================
# =============================================================================
# # PY4E-6.9-4
# print('banana'.count('a'))
# =============================================================================
# =============================================================================
# # PY4E-6.14-5
# string = 'X-DSPAM-Confidence:0.8475'
# string_after = string.split(':')
# print(float(string_after[1]))
# =============================================================================
# =============================================================================
# # PY4E-6.14-6
# print('   spacious   '.strip())
# print('www.example.com'.strip('cmowz.'))
# print('#....... Section 3.2.1 Issue #32 .......'.strip('.#! '))
# print('banana'.replace('a','b',1))
# print('banana'.replace('a','b'))
# =============================================================================
# =============================================================================
# # PY4E-7.11-1
# fname = input('Enter the file name:')
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened:',fname)
#     exit()
# count = 0
# for line in fhand:
#     line = line.rstrip().upper()
#     print(line)
#     count += 1
#     if count > 4:
#         break
# =============================================================================
# =============================================================================
# # PY4E-7.11-2
# fname = input('Enter the file name:')
# fhand = open(fname)
# total,count = 0,0
# for line in fhand:
#     if line.startswith('X-DSPAM-Confidence:'):
#         total += float(((line.rstrip()).split(':'))[1])
#         count += 1
# print(total/count)
# =============================================================================
# =============================================================================
# # PY4E-7.11-3
# import sys
# fname = input('Enter the file name:')
# if fname == 'na na boo boo':
#     print("NA NA BOO BOO TO YOU - You have been punk'd!")
#     sys.exit()
# try:
#     fhand = open(fname)
#     count = 0
#     for line in fhand:
#         if line.startswith('Subject:'):
#             count += 1
#     print('There were',count,'subject lines in',fname)
# except:
#     print('File cannot be opened:',fname)
# =============================================================================
# =============================================================================
# # PY4E-8.13-1
# def chop(list_unmodified):
#     list_unmodified[1:len(list_unmodified)-1]
#     return None
# def middle(list_unmodified):
#     a = list_unmodified[1:len(list_unmodified)-1]
#     return a
# a = [1,2,3,4,5,6,7,8,9]
# print(chop(a),middle(a))
# print(a)
# =============================================================================
# =============================================================================
# # PY4E-8.14-2
# fname = input('Enter the file name:')
# fhand = open(fname)
# for line in fhand:
#     words = line.split()
#     if len(words) == 0:continue
#     if(words[0]) != 'From':continue
#     if len(words) < 3:continue
#     print(words[2])
# =============================================================================
# =============================================================================
# # PY4E-8.14-3
# fname = input('Enter the file name:')
# fhand = open(fname)
# for line in fhand:
#     words = line.split()
#     if len(words) == 0 or (words[0]) != 'From' or len(words) < 3:continue
#     print(words[2])
# =============================================================================
# =============================================================================
# # PY4E-8.16-4
# fname = input('Enter file name:')
# try:
#     fhand = open(fname)
#     unique_words = []
#     for line in fhand:
#         temp = line.strip().split()
#         for word in temp:
#             if word not in unique_words:
#                 unique_words.append(word)
#     unique_words.sort()
#     print(unique_words)
# except:
#     print('File cannot be opened:',fname)
# =============================================================================
# =============================================================================
# # PY4E-8.16-5
# fname = input('Enter the file name:')
# try:
#     fhand = open(fname)
#     count = 0
#     for line in fhand:
#         # 'From ' is different from 'From:'
#         if not line.startswith('From '):continue
#         count += 1
#         print(line.strip().split()[1])
#     print('There were',count,'lines in the file with From as the first word')
# except:
#     print('File cannot be opened:',fname)
# =============================================================================
# =============================================================================
# # PY4E-8.16-6
# numb = []
# while True:
#     a = input('Enter a number:')
#     if a == 'done':
#         break
#     numb.append(a)
# print('Maximum:',float(max(numb)))
# print('Minimum:',float(min(numb)))
# =============================================================================
# =============================================================================
# a = (1,2,3,4,5,6,7,8,9)
# print(sum(a))
# print(sum(a)/len(a))
# L = [1,2,3]
# print(L)
# L.append(L)
# print(L)
# print(L[-3])
# print(L is L[-1])
# =============================================================================
# PY4E-5
# largest = None
# smallest = None
# while True:
#     try:
#         num = input('Enter a number:')
#         if num == 'done':
#             break
#         num = int(num)
#         if largest == None or num > largest:
#             largest = num
#         if smallest == None or num < smallest:
#             smallest = num
#         continue
#     except:
#         print('Invalid input')
#         continue
# print('Maximum is',largest)
# print('Minimum is',smallest)
# PY4E-6.5
# text = "X-DSPAM-Confidence:    0.8475"
# num = text.find(':')
# a = text[num + 1 :].split()[0]
# a = float(a)
# print(a)
# PY4E-7.2
# fname = input('Enter file name:')
# fhand = open(fname)
# total = 0
# count = 0
# for line in fhand:
#     if not line.startswith("X-DSPAM-Confidence:"):
#         continue
#     num = line.find(':')
#     total += float(line[num + 1:].split()[0])
#     count += 1
# print('Average spam confidence:',total/count)
# import copy
# L = [2]
# L1 = [L]
# L2 = [[L1]]
# L3 = copy.deepcopy(L2)
# L.append(3)
# print(f'L1 = {L1},L2 = {L2},L3 = {L3}')
# L1 = [2]
# L2 = [L1,L1]
# L3 = copy.deepcopy(L2)
# L3[0].append(3)
# print(L3)
# L1 = [2]
# L1.append(L1)
# print(L1[1][1][1])
# a = [x for x in range(2, 100) if not all((x % y) != 0 for y in range(2, x))]
# print(a)
# def f(L1,L2):
# """_summary_
# L1,L2 lists of same length of numbers
# returns the sum of raising each element in L1
# to the power of the element at the same index in L2
# For example, f([1,2],[2,3]) returns 9
# """
# total = 0
# for i in map(lambda x,y:x**y, L1,L2):
# total += i
# return total
# print(f([1,2], [2,3]))
# def get_mid(d):
#     """
#     returns the value in d with the key that occurs first in the alphabet.
#     E.g., if d = {x = 11, b = 12},get_min returns 12.
#     Args:
#     d (dict): a dict mapping letters to ints
#     """
#     a = []
#     for key,val in d.items():
#         a.append(key)
#     a.sort()
#     return d[a[0]]
# print(get_mid({'x': 11,'b': 12}))
# Finger exercise-5.9
# fhand = open('D:\\0 Abel\Code\Python_Code\\Don Quixote.txt')
# fhand = open('Don Quixote.txt')
# book = fhand.read()
# cipher_text = '1*13*2*6*57*2*1*13'
# try:
# gen_decode_keys = lambda book, cipher_text: {
# s: book[int(s)] for s in cipher_text.split('*')
# }
# print(gen_decode_keys(book, cipher_text))
# except:
# print('Please change another book.')
# gen_code_keys = lambda book, plain_text: ({c: str(book.find(c)) for c in plain_text})
# encode = lambda code_keys, plain_text: ''.join(
#     ['*' + code_keys[c] for c in plain_text]
# )[1:]
# encrypt = lambda book, plain_text: encode(gen_code_keys(book, plain_text), plain_text)
# Finger exercise-5.8
# fhand = open('Don Quixote.txt')
# book = fhand.read()
# cipher_text = '22*13*33*137*59*11*23*11*1*57*6*13*1*2*6*57*2*6*1*22*13*33*137*59*11*23*11*1*57*6*173*7*11'
# gen_decode_keys = lambda book, cipher_text: {
#     s: book[int(s)] for s in cipher_text.split('*')
# }
# decode = lambda decode_keys, cipher_text: ''.join(
#     ['' + decode_keys[c] for c in cipher_text.split('*')][:]
# )
# decrypt = lambda book, cipher_text: decode(
#     gen_decode_keys(book, cipher_text), cipher_text
# )
# print(decrypt(book, cipher_text))
# Finger exercise-6.0
# def harmonic_sum(n):
#     """The harmonic sum of an integer,returns the sum
#     Args:
#         n (int): number of integer,n>0
#     """
#     if n == 1:
#         return n
#     else:
#         return 1 / n + harmonic_sum(n - 1)


# print(harmonic_sum(4))
# Finger exercise-7.1
# import calendar as cal
# def shopping_days(year):
#     """returns the number of days between U.S. Thanksgiving and Christmas in year
#     Args:
#         year (int): year a number >= 1941
#     """
#     month = cal.monthcalendar(year, 11)
#     if month[0][cal.THURSDAY] != 0:
#         thanksgiving = month[3][cal.THURSDAY]
#     else:
#         thanksgiving = month[4][cal.THURSDAY]
#     return (25 + (30 - thanksgiving))


# print(shopping_days(2023))
# Finger exercise-7.2
# import calendar as cal
# def canadian_days(year):
#     """returns the number of days between Canadian Thanksgiving and Christmas
#     Args:
#         year (int): year > 1957
#     """
#     month = cal.monthcalendar(year, 10)
#     if month[0][cal.MONDAY] != 0:
#         thanksgiving = month[1][cal.MONDAY]
#     else:
#         thanksgiving = month[2][cal.MONDAY]
#     return 25 + 30 + (31 - thanksgiving)
# print(canadian_days(2023))
# Finger exercise-7.3
# def fibonacci(n):
#     """generate a Fibonacci sequence from 1 to n
#     Args:
#         n (int): the number of Fibonacci sequence
#     """
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)


# fib_file = open('fib_file.txt', 'w')
# for i in range(1, 11):
#     fib_file.writelines(f'{fibonacci(i)}\n')
# # close the file and the program can store the information that can be read
# fib_file.close()
# print(open('fib_file.txt').read())
# PY4E-9-1
# fhand = open('words.txt')
# words = {}
# for line in fhand:
#     line = line.lower().split()
#     for word in line:
#         words[word] = words.get(word, 0) + 1
# print(words)
# print('right' in words)
# PY4E-9-2
# fname = input('Enter file name:')
# fhand = open(fname)
# day = {}
# for line in fhand:
#     if line.startswith('From') and len(line.split()) > 3:
#         word = line.strip().split()[2]
#         day[word] = day.get(word, 0) + 1
# print(day)
# PY4E-9-3
# fname = input('Enter file name:')
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened:',fname)
#     exit()
# histogram = {}
# for line in fhand:
#     if (not line.startswith('Author')) or (line.find('@') == -1):
#         continue
#     words = line.rstrip().split()
#     for word in words:
#         if word.find('@') != -1:
#             histogram[word] = histogram.get(word, 0) + 1
# print(histogram)
# PY4E-9-4
# fname = input('Enter file name:')
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened:', fname)
#     exit()
# histogram = {}
# for line in fhand:
#     if (not line.startswith('Author')) or (line.find('@') == -1):
#         continue
#     words = line.rstrip().split()
#     for word in words:
#         if word.find('@') != -1:
#             histogram[word] = histogram.get(word, 0) + 1
# max_key = max(histogram, key=histogram.get)
# print(max_key, histogram.get(max_key))
# PY4E-9-5
# fname = input('Enter file name:')
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened:', fname)
#     exit()
# histogram = {}
# for line in fhand:
#     if (not line.startswith('Author')) or (line.find('@') == -1):
#         continue
#     words = line.rstrip().split()
#     for word in words:
#         if word.find('@') != -1:
#             word = word.split('@')[1]
#             histogram[word] = histogram.get(word, 0) + 1
# print(histogram)
# PY4E-10-1
# fname = input('Enter file name:')
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened:', fname)
#     exit()
# histogram = {}
# for line in fhand:
#     if (not line.startswith('Author')) or (line.find('@') == -1):
#         continue
#     words = line.rstrip().split()
#     for word in words:
#         if word.find('@') != -1:
#             histogram[word] = histogram.get(word, 0) + 1
# count = list(histogram.items())
# count.sort(key = lambda x:x[1],reverse=True)
# print(count[0][0], count[0][1])
# PY4E-10-2
# fname = input('Enter file name:')
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened:', fname)
#     exit()
# histogram = {}
# for line in fhand:
#     if (not line.startswith('From')) or (len(line.split()) < 6):
#         continue
#     line = line.rstrip().split()[5]
#     time = line.split(':')[0]
#     histogram[time] = histogram.get(time, 0) + 1
# count = list(histogram.items())
# count.sort()
# for key, val in count:
#     print(key, val)
# PY4E-10-3
# import string
# fname = input('Enter file name:')
# try:
#     fhand = open(fname,error = 'ignore')
# except:
#     print('File cannot be opened:', fname)
#     exit()
# frequency_letter = {}
# total = 0
# for line in fhand:
#     line = line.translate(str.maketrans('', '', string.punctuation))
#     line = line.rstrip().lower().split()
#     for word in line:
#         for letter in word:
#             if not letter.islower():
#                 continue
#             frequency_letter[letter] = frequency_letter.get(letter, 0) + 1
#             total += 1
# count = list(frequency_letter.items())
# count.sort(key=lambda x: x[1], reverse=True)
# for key, val in count:
#     print(key, val/total)
# PY4E-11-1
# import re
# fname = input('Enter file name:')
# fname = 'mbox.txt'
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened:', fname)
#     exit()
# count = 0
# regular_expression = input('Enter a regular expression:')
# for line in fhand:
#     line = line.rstrip()
#     if re.findall(regular_expression, line):
#         count += 1
# print(fname, 'had', count, 'lines that matched', regular_expression)
# PY4E-11-2
# import re
# fname = input('Enter file name:')
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened', fname)
#     exit()
# total = 0
# count = 0
# for line in fhand:
#     line = line.strip()
#     version = re.findall('^New\sRevision:\s([0-9]+)', line)
#     if len(version) < 1:
#         continue
#     #convert list to string
#     version = ''.join(str(elem) for elem in version)
#     total += int(version)
#     count += 1
# print(int(total / count))
# PY4E-12-1
import socket
import re

url = input('Enter the URL:')
try:
    domain = re.findall('http[s]?://(.*?)/.*', url)
    domain = ''.join(str(elem) for elem in domain)
    print(domain)
except:
    print('Improperly formatted or non-existent URL:',url)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
mysock.connect((domain, 80))
mysock.send(cmd)
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()
