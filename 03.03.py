"""
Выведите все элементы списка с четными индексами
(то есть A[0], A[2], A[4], ...).
"""

a = input().split()

for i in range(0, len(a), 2):
    print(a[i])

"""
Выведите все четные элементы списка.
"""

lst = input().split()

for item in lst:
    if int(item) % 2 == 0:
        print(item)

"""
Найдите количество положительных (>0) элементов 
в данном списке.
"""

lst = input().split()

for item in lst:
    if int(item) > 0:
        print(item)

"""
Дан список чисел. Выведите все элементы списка, 
которые больше предыдущего элемента.
"""

lst = input().split()
a = lst[0]

for i in range(1, len(lst)):
    if int(lst[i]) > int(a):
        print(lst[i])
    a = lst[i]

"""
Дан список чисел. 
Если в нем есть два соседних элемента одного знака,
выведите эти числа. Если соседних элементов 
одного знака нет - не выводите ничего. 
Если таких пар соседей несколько - выведите первую пару.
"""

lst = input().split()

for i in range(1, len(lst)):
    if int(lst[i]) * int(
            lst[i - 1]) > 0:  # проверяем, больше ли нуля произведение текущего элемента и предыдущего элемента
        print(lst[i - 1], lst[i])  # мы находим пару соседних элементов с одинаковым знаком
        break

"""
Дан список чисел. Определите, сколько 
в этом списке элементов,
которые больше двух своих соседей и 
выведите количество таких элементов.
"""

lst = input().split()
count = 0
for i in range(1, len(lst)-1):
    if int(lst[i]) > int(lst[i-1]) and int(lst[i]) > int(lst[i+1]):
        count += 1
print(count)

"""
Дан список чисел. Выведите значение наибольшего элемента в списке, 
а затем индекс этого элемента в списке. 
Если наибольших элементов несколько, 
выведите индекс первого из них.
"""

maxс = 0
lst = input().split()
for i in range(1, len(lst)):
    if int(lst[i]) > int(lst[maxс]):
        maxс = i
print(lst[maxс], maxс)

"""
Выведите значение наименьшего из 
всех положительных элементов в списке. 
"""
lst = list(map(int, input().split()))
min_pos = None

for numb in lst:
    if numb > 0:
        if min_pos is None or numb < min_pos:
            min_pos = numb
print(min_pos)

"""
Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю. 
Помогите ему это сделать.
Входные данные
Программа получает на вход невозрастающую последовательность натуральных чисел, означающих рост каждого человека в строю. 
После этого вводится число X – рост Пети. 
Все числа во входных данных натуральные и не превышают 200.
Выходные данные
Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с одинаковым ростом, таким же, как у Пети, 
то он должен встать после них.
"""

heights = input().split() #мы считываем последовательность высот из входных данных
petya_height = int(input()) #высота пети

index = len(heights)
for i in range(len(heights)):
    if int(heights[i]) < petya_height:
        index = i
        break

heights.insert(index, petya_height)
count = len(heights) - index
print(count)

"""
Выведите элементы данного списка 
в обратном порядке, не изменяя сам список.
"""
lst = input().split()

for i in range(len(lst)-1, -1, -1):
    print(lst[i])
