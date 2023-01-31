'''Решение задач без использования операторов (усл. данное на семинар)
'''


a = int(input())
b = int(input())
c = (a ** 2 + b ** 2) ** 0.5
print(c)  # Task1

name = str(input())
print('Hello, ' + name + '!')  # Task2

a = int(input())
b = a + 1
c = a - 1
print('The next number for the number ' + str(a) + ' is ' + str(b) + '.')
print('The previous number for the number ' + str(a) + ' is ' + str(c) + '.')  # Task3

n = int(input())
k = int(input())
c = n // k
print(k)  # Task4

n = int(input())
k = int(input())
c = n % k
print(c)  # Task5

a = int(input())
print(a % 10)  # Task6

a = int(input())
print(a % 10)  # Task7

n = int(input())
print(n // 10 % 10)  # Task8

n = int(input())
print(n // 100 + n // 10 % 10 + n % 10)  # Task9

n = int(input())
print(n + 2 - (n % 2))  # Task10

a = int(input())
b = int(input())
c = int(input())
d = a + b + c
print((d + 2 - 1) // 2)  # Task M

n = int(input())
a = n // 60
b = n % 60
print(a, b)  # Task N

a = int(input())
b = int(input())
a, b = b, a
print(a, b)  # Task P

a = int(input())
b = int(input())
a, b = b, a
print(a, b)  # Task Q

n = int(input())
m = int(input())
print(m // n)  # Task U

h = int(input())
a = int(input())
b = int(input())
print((h - a) / (a - b) + 1)  # Task W

n = int(input())
print(n // 1000 - n % 10 + n // 100 % 10 - n // 10 % 10 + 1) #Task X

n = int(input())
m = int(input())
print(n % m + 1)  # Task Y


