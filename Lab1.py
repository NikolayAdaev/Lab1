# Импорт необходимых модулей
import random
import time
import math

class game:
    def __init__(self):
     self.players = []
     self.scores = {}
     self.rounds = 0
    def addPlayer(self, player):
     self.players.append(player)
     self.scores[player] = 0
    def playRound(self):
     print("Round", self.rounds +1)
     for player in self.players:
      score = random.randint(1,6)
      self.scores[player] += score
      print(player,"scored",score)
     self.rounds +=1
    def getWinner(self):
     winner = None
     max_score = 0
     for player in self.players:
      if self.scores[player] > max_score:
       max_score = self.scores[player]
       winner = player
     return winner, max_score
    def start(self):
     while self.rounds <10:
      self.playRound()
      time.sleep(0.5)
     winner, score = self.getWinner()
     print("The winner is",winner,"with a score of",score)
     self.showFinalScores()
    def showFinalScores(self):
     print("Final Scores:")
     for player in self.players:
      print(player,":",self.scores[player])

if __name__=="__main__":
    g = game()
    g.addPlayer("Alice")
    g.addPlayer("Bob")
    g.addPlayer("Charlie")
    g.addPlayer("Dave")
    g.start()

# Дополнительные функции

def helperFunction(x):
 if x > 0:
  return x * helperFunction(x -1)
 else:
  return 1

for i in range(10):
 print("Factorial of", i, "is", helperFunction(i))

# Еще немного кода для увеличения объема

def calculate(a,b,c):
 result = a+b*c
 if result > 100:
  print("Large number")
 else:
  print("Result is", result)
 return result

nums = [i for i in range(10, 100, 10)]
for num in nums:
 res = calculate(num, num+1, num+2)
 print("Calculation result:", res)

# Класс с ошибками оформления

class person:
 def __init__(self,name,age):
  self.name=name
  self.age=age
 def greet(self):
  print("Hello, my name is",self.name)
  print("I am",self.age,"years old")
 def isAdult(self):
  if self.age>=18:
   return True
  else:
   return False
 def birthday(self):
  self.age+=1
  print("Happy Birthday!",self.name,"You are now",self.age)

p = person("Eve",17)
p.greet()
if p.isAdult():
 print(p.name,"is an adult.")
else:
 print(p.name,"is not an adult.")
p.birthday()

# Добавим больше классов и функций с ошибками

class calculator:
 def add(self,a,b):
  return a+b
 def subtract(self,a,b):
  return a-b
 def multiply(self,a,b):
  return a*b
 def divide(self,a,b):
  if b!=0:
   return a/b
  else:
   print("Cannot divide by zero")
   return None
 def power(self,a,b):
  return a**b

calc = calculator()
print("Addition:", calc.add(5,3))
print("Subtraction:", calc.subtract(5,3))
print("Multiplication:", calc.multiply(5,3))
print("Division:", calc.divide(5,0))
print("Power:", calc.power(5,3))

# Функции для работы со строками

def reverseString(s):
 return s[::-1]

def isPalindrome(s):
 return s == s[::-1]

strings = ["radar", "hello", "level", "world", "madam"]
for s in strings:
 print("Original:", s, "Reversed:", reverseString(s))
 if isPalindrome(s):
  print(s, "is a palindrome")
 else:
  print(s, "is not a palindrome")

# Работа с файлами

def writeToFile(filename, data):
 f = open(filename, 'w')
 f.write(data)
 f.close()

def readFromFile(filename):
 f = open(filename, 'r')
 content = f.read()
 f.close()
 return content

writeToFile('test.txt', 'Hello, World!')
print("Content of file:", readFromFile('test.txt'))

# Генерация числовых последовательностей

def fibonacci(n):
 seq = [0,1]
 for i in range(2,n):
  seq.append(seq[i-1]+seq[i-2])
 return seq

print("Fibonacci sequence:", fibonacci(10))

# Работа с матрицами

def createMatrix(rows, cols):
 matrix = []
 for i in range(rows):
  row = []
  for j in range(cols):
   row.append(random.randint(1,10))
  matrix.append(row)
 return matrix

def printMatrix(matrix):
 for row in matrix:
  for elem in row:
   print(elem, end=' ')
  print()

matrix = createMatrix(3,3)
print("Matrix:")
printMatrix(matrix)

# Обработка ошибок

def divideNumbers(a,b):
 try:
  result = a / b
  print("Result:", result)
 except ZeroDivisionError:
  print("Error: Division by zero")

divideNumbers(10, 2)
divideNumbers(10, 0)

# Использование lambda функций

nums = [1,2,3,4,5]
squared = list(map(lambda x: x**2, nums))
print("Squared numbers:", squared)

# Работа с списками

def filterEvenNumbers(numbers):
 even_numbers = []
 for num in numbers:
  if num % 2 == 0:
   even_numbers.append(num)
 return even_numbers

numbers = [i for i in range(1,21)]
print("Even numbers:", filterEvenNumbers(numbers))

# Пример рекурсии

def sumToN(n):
 if n > 0:
  return n + sumToN(n-1)
 else:
  return 0

print("Sum to 10:", sumToN(10))

# Класс для работы с комплексными числами

class complexNumber:
 def __init__(self, real, imag):
  self.real = real
  self.imag = imag
 def add(self, other):
  return complexNumber(self.real + other.real, self.imag + other.imag)
 def __str__(self):
  return f"{self.real} + {self.imag}i"

c1 = complexNumber(2,3)
c2 = complexNumber(4,5)
c3 = c1.add(c2)
print("Complex number addition:", c3)

# Работа с словарями

def countLetters(s):
 letter_count = {}
 for letter in s:
  if letter in letter_count:
   letter_count[letter] +=1
  else:
   letter_count[letter]=1
 return letter_count

print("Letter count:", countLetters("hello world"))

# Обработка списков списков

def flattenList(lst):
 flat_list = []
 for sublist in lst:
  for item in sublist:
   flat_list.append(item)
 return flat_list

nested_list = [[1,2],[3,4],[5,6]]
print("Flattened list:", flattenList(nested_list))

# Использование *args и **kwargs

def printArgs(*args, **kwargs):
 print("Positional arguments:", args)
 print("Keyword arguments:", kwargs)

printArgs(1,2,3, a=4, b=5)

# Завершаем код для соответствия требуемому количеству строк

# Функции для работы с датами и временем

import datetime

def getCurrentDateTime():
 now = datetime.datetime.now()
 print("Current date and time:", now)

getCurrentDateTime()

def formatDate(date):
 return date.strftime("%Y-%m-%d")

today = datetime.date.today()
print("Formatted date:", formatDate(today))

# Пример использования генераторов

def simpleGenerator():
 yield 1
 yield 2
 yield 3

for value in simpleGenerator():
 print("Generated value:", value)

# Работа с множествами

def uniqueElements(lst):
 return set(lst)

print("Unique elements:", uniqueElements([1,2,2,3,4,4,5]))

# Работа с очередью

from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print("Queue elements:", list(queue))
queue.popleft()
print("Queue after pop:", list(queue))

# Работа с стэком

stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print("Stack elements:", stack)
stack.pop()
print("Stack after pop:", stack)

# Работа с регулярными выражениями

import re

def findEmails(text):
 emails = re.findall(r'\S+@\S+', text)
 return emails

sample_text = "Contact us at info@example.com or support@example.org"
print("Found emails:", findEmails(sample_text))

# Работа с JSON

import json

data = {'name': 'John', 'age': 30, 'city': 'New York'}
json_str = json.dumps(data)
print("JSON string:", json_str)
data_loaded = json.loads(json_str)
print("Loaded data:", data_loaded)

# Работа с XML

import xml.etree.ElementTree as ET

root = ET.Element("root")
child = ET.SubElement(root, "child")
child.text = "This is a child element"
tree = ET.ElementTree(root)
ET.dump(tree)

# Работа с CSV

import csv

with open('data.csv', 'w', newline='') as csvfile:
 writer = csv.writer(csvfile)
 writer.writerow(['Name', 'Age'])
 writer.writerow(['Alice', 30])
 writer.writerow(['Bob', 25])

with open('data.csv', 'r') as csvfile:
 reader = csv.reader(csvfile)
 for row in reader:
  print("CSV row:", row)

# Работа с декораторами

def my_decorator(func):
 def wrapper(*args, **kwargs):
  print("Before function call")
  result = func(*args, **kwargs)
  print("After function call")
  return result
 return wrapper

@my_decorator
def sayHello(name):
 print("Hello", name)

sayHello("Alice")

# Работа с конфигурационными файлами

import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {'Server': 'localhost', 'Port': '8080'}
with open('config.ini', 'w') as configfile:
 config.write(configfile)

config.read('config.ini')
print("Config Server:", config['DEFAULT']['Server'])
