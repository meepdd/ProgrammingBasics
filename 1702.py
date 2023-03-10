"""
Даны два целых числа A и B (при этом A ≤ B).
Выведите все числа от A до B включительно.
"""

a = int(input())
b = int(input())

for i in range (a, b+1):
    print(i)

"""
Даны два целых числа A и В. Выведите 
все числа от A до B включительно, 
в порядке возрастания, если A < B, 
или в порядке убывания в противном случае.
"""


a = int(input())
b = int(input())

if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range (a, b-1, -1):
        print(i)

"""
Дано натуральное число n. 
Напечатайте все n-значные нечетные натуральные числа
в порядке убывания.
"""
n = int(input())

for i in range(10 ** n, 10 ** (n - 1) - 1, -1):
    if i % 2 != 0:
        print(i)
"""
По данному натуральном 𝑛 вычислите сумму 12+22+32+...+𝑛2
"""

n = int(input())
count = 0

for i in range(1, n + 1):
    count += i ** 2

print(count)

"""
По данному натуральному n вычислите сумму 1^3+2^3+3^3+…+n3.
"""

n = int(input())
count = 0

for i in range(1, n + 1):
    count += i ** 3

print(count)

"""
По данному целому неотрицательному n вычислите значение n!.
"""
n = int(input())

factorial = 1

for i in range(2, n + 1):
    factorial *= i

print(factorial)

"""
Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n пингвинов. 
Изображение одного пингвина имеет размер 5×9 символов, 
между двумя соседними пингвинами также имеется пустой (из пробелов) столбец. 
Разрешается вывести пустой столбец после последнего пингвина. 
Для упрощения рисования скопируйте пингвина из примера в среду разработки.
"""

chel = [
  '   _~_    ',
  '  (o o)   ',
  ' /  V  \\  ',
  '/(  _  )\\ ',
  '  ^^ ^^   '
]
a = int(input())
while a <= 9:
    for i in chel:
        print(a * i, )
else:
    print('You enter number >9')

"""
По данным двум натуральным числам A и B (A≤B) 
выведите все чётные числа на отрезке от A до B. 
В этой задаче нельзя использовать инструкцию if.
"""

a = int(input())
b = int(input())
for i in range(a, b-(b % 2)+1, 2):
  print(i % 2 + i)

"""
Дано 10 целых чисел. 
Вычислите их сумму. Напишите программу, 
использующую наименьшее число переменных.
"""
sum = 0
for i in range(10):
    numb = int(input())
    sum += numb
print(sum)


"""
Дано несколько чисел. Вычислите их сумму. 
Сначала вводите количество чисел N, затем вводится ровно N целых чисел. 
Какое наименьшее число переменных нужно для решения этой задачи?
"""
n = int(input())

sum = 0

for i in range(n):
    sum += int(input())
print(sum)

"""
Дано несколько чисел. Подсчитайте, 
сколько из них равны нулю, 
и выведите это количество.
"""
n = int(input())
count = 0
for i in range(n):
    a = int(input())
    if a == 0:
        count += 1
    else:
        count += 0
print(count)

"""
По данному натуральному n≤9 выведите лесенку из n ступенек, 
i-я ступенька состоит из чисел от 1 до i без пробелов.
"""
n = int(input())

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j)
    print()

"""
По данному натуральном 𝑛 вычислите сумму 1!+2!+3!+...+𝑛!.
В решении этой задачи можно использовать только один цикл.
"""
n = int(input())

factorial = 1
sum = 1

for i in range(2, n + 1):
    sum += factorial * i
    factorial *=i
print(sum)

