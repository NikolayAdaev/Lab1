import random
import time
import math


class Game:
    def __init__(self):
        self.players = []
        self.scores = {}
        self.rounds = 0

    def add_player(self, player):
        self.players.append(player)
        self.scores[player] = 0

    def play_round(self):
        print("Round", self.rounds + 1)
        for player in self.players:
            score = random.randint(1, 6)
            self.scores[player] += score
            print(player, "scored", score)
        self.rounds += 1

    def get_winner(self):
        winner = None
        max_score = 0
        for player in self.players:
            if self.scores[player] > max_score:
                max_score = self.scores[player]
                winner = player
        return winner, max_score

    def start(self):
        while self.rounds < 10:
            self.play_round()
            time.sleep(0.5)
        winner, score = self.get_winner()
        print("The winner is", winner, "with a score of", score)
        self.show_final_scores()

    def show_final_scores(self):
        print("Final Scores:")
        for player in self.players:
            print(player, ":", self.scores[player])


if __name__ == "__main__":
    g = Game()
    g.add_player("Alice")
    g.add_player("Bob")
    g.add_player("Charlie")
    g.add_player("Dave")
    g.start()


# Дополнительные функции

def helper_function(x):
    if x > 0:
        return x * helper_function(x - 1)
    else:
        return 1


for i in range(10):
    print("Factorial of", i, "is", helper_function(i))


# Еще немного кода для увеличения объема

def calculate(a, b, c):
    result = a + b * c
    if result > 100:
        print("Large number")
    else:
        print("Result is", result)
    return result


nums = [i for i in range(10, 100, 10)]
for num in nums:
    res = calculate(num, num + 1, num + 2)
    print("Calculation result:", res)


# Класс с ошибками оформления

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name)
        print("I am", self.age, "years old")

    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False

    def birthday(self):
        self.age += 1
        print("Happy Birthday!", self.name, "You are now", self.age)


p = Person("Eve", 17)
p.greet()
if p.is_adult():
    print(p.name, "is an adult.")
else:
    print(p.name, "is not an adult.")
p.birthday()


# Добавим больше классов и функций с ошибками

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            print("Cannot divide by zero")
            return None

    def power(self, a, b):
        return a ** b


calc = Calculator()
print("Addition:", calc.add(5, 3))
print("Subtraction:", calc.subtract(5, 3))
print("Multiplication:", calc.multiply(5, 3))
print("Division:", calc.divide(5, 0))
print("Power:", calc.power(5, 3))


# Функции для работы со строками

def reverse_string(s):
    return s[::-1]


def is_palindrome(s):
    return s == s[::-1]


strings = ["radar", "hello", "level", "world", "madam"]
for s in strings:
    print("Original:", s, "Reversed:", reverse_string(s))
    if is_palindrome(s):
        print(s, "is a palindrome")
    else:
        print(s, "is not a palindrome")


# Работа с файлами

def write_to_file(filename, data):
    f = open(filename, 'w')
    f.write(data)
    f.close()


def read_from_file(filename):
    f = open(filename, 'r')
    content = f.read()
    f.close()
    return content


write_to_file('test.txt', 'Hello, World!')
print("Content of file:", read_from_file('test.txt'))


# Генерация числовых последовательностей

def fibonacci(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[i - 1] + seq[i - 2])
    return seq


print("Fibonacci sequence:", fibonacci(10))


# Работа с матрицами

def create_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.randint(1, 10))
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end=' ')
        print()


matrix = create_matrix(3, 3)
print("Matrix:")
print_matrix(matrix)


# Обработка ошибок

def divide_numbers(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero")


divide_numbers(10, 2)
divide_numbers(10, 0)


# Использование lambda функций

nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, nums))
print("Squared numbers:", squared)


# Работа с списками

def filter_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers


numbers = [i for i in range(1, 21)]
print("Even numbers:", filter_even_numbers(numbers))


# Пример рекурсии

def sum_to_n(n):
    if n > 0:
        return n + sum_to_n(n - 1)
    else:
        return 0


print("Sum to 10:", sum_to_n(10))


# Класс для работы с комплексными числами

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def add(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"


c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(4, 5)
c3 = c1.add(c2)
print("Complex number addition:", c3)


# Работа с словарями

def count_letters(s):
    letter_count = {}
    for letter in s:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count


print("Letter count:", count_letters("hello world"))


# Обработка списков списков

def flatten_list(lst):
    flat_list = []
    for sublist in lst:
        for item in sublist:
            flat_list.append(item)
    return flat_list


nested_list = [[1, 2], [3, 4], [5, 6]]
print("Flattened list:", flatten_list(nested_list))


# Использование *args и **kwargs

def print_args(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)


print_args(1, 2, 3, a=4, b=5)


# Функции для работы с датами и временем

import datetime


def get_current_date_time():
    now = datetime.datetime.now()
    print("Current date and time:", now)


get_current_date_time()


def format_date(date):
    return date.strftime("%Y-%m-%d")


today = datetime.date.today()
print("Formatted date:", format_date(today))


# Пример использования генераторов

def simple_generator():
    yield 1
    yield 2
    yield 3


for value in simple_generator():
    print("Generated value:", value)


# Работа с множествами

def unique_elements(lst):
    return set(lst)


print("Unique elements:", unique_elements([1, 2, 2, 3, 4, 4, 5]))


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


def find_emails(text):
    emails = re.findall(r'\S+@\S+', text)
    return emails


sample_text = "Contact us at info@example.com or support@example.org"
print("Found emails:", find_emails(sample_text))


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
def say_hello(name):
    print("Hello", name)


say_hello("Alice")


# Работа с конфигурационными файлами

import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {'Server': 'localhost', 'Port': '8080'}
with open('config.ini', 'w') as configfile:
    config.write(configfile)

config.read('config.ini')
print("Config Server:", config['DEFAULT']['Server'])
