"""
Даны четыре действительных числа: 𝑥1, 𝑦1, 𝑥2,𝑦2.
Напишите функцию distance(x1, y1, x2, y2),
вычисляющую расстояние между точкой (𝑥1,𝑦1).
Считайте четыре действительных числа и выведите результат работы этой функции.
"""
x_1 = float(input())
x_2 = float(input())
y_1 = float(input())
y_2 = float(input())


def find_x(x_1, y_1, x_2, y_2):
    return ((((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5))


print(find_x(x_1, y_1, x_2, y_2))

"""
Напишите функцию min4(a, b, c, d),
вычисляющую минимум четырех чисел,
которая не содержит инструкции if,
а использует стандартную функцию min.
Считайте четыре целых числа и выведите их минимум.
"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())


def min4(a, b, c, d):
    return (min(a, b, c, d))


print(min4(a, b, c, d))

"""
Даны два действительных числа 𝑥 и 𝑦.
Проверьте, принадлежит ли точка с координатами (𝑥,𝑦)
заштрихованному квадрату (включая его границу).
Если точка принадлежит квадрату, выведите слово YES,
иначе выведите слово NO.
На рисунке сетка проведена с шагом 1.
"""
x = float(input())
y = float(input())


def IsPointInSquare(x, y):
    return (-1 <= x <= 1) and (-1 <= y <= 1) and "YES" or "NO"


print(IsPointInSquare(x, y))

"""
Даны два действительных числа 𝑥 и 𝑦.
Проверьте, принадлежит ли точка с координатами (𝑥,𝑦)
заштрихованному квадрату (включая его границу).
Если точка принадлежит квадрату, выведите слово YES,
иначе выведите слово NO.
На рисунке сетка проведена с шагом 1.
"""

x = float(input())
y = float(input())


def IsPointInSquare(x, y):
    return abs(x) + abs(y) <= 1 and "YES" or "NO"


print(IsPointInSquare(x, y))

"""
Даны пять действительных чисел: 𝑥, 𝑦, 𝑥𝑐, 𝑦𝑐, 𝑟.
Проверьте, принадлежит ли точка (𝑥,𝑦) кругу с центром (𝑥𝑐,𝑦𝑐).
Если точка принадлежит кругу,
выведите слово YES, иначе выведите слово NO.
Решение должно содержать функцию IsPointInCircle(x, y, xc, yc, r),
возвращающую True, если точка принадлежит кругу и False,
если не принадлежит. Основная программа должна считать координаты точки,
вызвать функцию IsPointInCircle и в зависимости от возвращенного значения вывести на экран
необходимое сообщение.
Функция IsPointInCircle не должна содержать инструкцию if.
"""
x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())


def IsPointInCircle(x, y, xc, yc, r):
    return (x - xc) ** 2 + (y - yc) ** 2 <= r ** 2 and "YES" or "NO"


print(IsPointInCircle(x, y, xc, yc, r))

"""
Дано действительное положительное число 𝑎 и целоe число 𝑛.
Вычислите 𝑎𝑛. Решение оформите в виде функции power(a, n).

Стандартной функцией или операцией возведения в степень пользоваться нельзя.
"""
a = float(input())
n = int(input())


def power(a, n):
    if n == 0:
        return 1
    elif n > 0:
        return a * power(a, n - 1)
    else:
        return 1 / power(a, -n)


print(power(a, n))

"""
Даны два натуральных числа 𝑛 и 𝑚. Сократите дробь 𝑛𝑚,
то есть выведите два других числа 𝑝 таких, что 𝑛𝑚=𝑝𝑞 и дробь 𝑝𝑞
 — несократимая.

Решение оформите в виде функции ReduceFraction(n, m),
получающая значения n и m и возвращающей кортеж из двух чисел.
"""
n = int(input())
m = int(input())


def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)


def ReduceFraction(n, m):
    d = gcd(n, m)
    p = n // d
    q = m // d
    return (p, q)


print(ReduceFraction(n, m))

"""
Дано натуральное число 𝑛>1. 
Выведите его наименьший простой делитель.
Решение оформите в виде функции MinDivisor(n). 
Алгоритм должен иметь сложность 𝑂(𝑛√)
Указание. Если у числа 𝑛 нет делителя не превосходящего 𝑛√, 
то число 𝑛 — простое и ответом будет само число 𝑛
"""
n = int(input())


def MinDivisor(n):
    for i in range(2, n + 1):
        if n % i == 0:
            return i
        return n


print(MinDivisor(n))

"""
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.
"""
a = int(input())
b = int(input())


def sum(a, b):
    if b == 0:
        return a
    return sum(a + 1, b - 1)


print(sum(a, b))

"""
Напишите функцию phib(𝑛), которая по данному целому неотрицательному n возвращает 𝑛-e число Фибоначчи.
В этой задаче нельзя использовать циклы - используйте рекурсию.
phib(1) = phib(2) = 1
phib(n) = phib(n - 1) + phib(n - 2)
"""
n = int(input())


def phib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return phib(n - 1) + phib(n - 2)


print(phib(n))

"""
По данным числам 𝑛 и 𝑘(0≤𝑘≤𝑛) вычислите С𝑘𝑛.
Для решения используйте рекуррентное соотношение 𝐶𝑘𝑛=𝐶𝑘−1𝑛−1+𝐶𝑘𝑛−1
Решение оформите в виде функции C(n, k).
"""
n = int(input())
k = int(input())


def C(n, k):
    if 0 <= k <= n:
        return C(n - 1, k) + C(n - 1, k - 1)
    if k == 0:
        return 1
    else:
        return 0


print(C(n, k))

"""
Дана последовательность чисел, завершающаяся числом 0.
Найдите сумму всех этих чисел, не используя цикл.
"""


def seq():
    n = int(input())
    if n != 0:
        return n + seq()
    return 0


print(seq())

"""
Дана последовательность целых чисел,
заканчивающаяся числом 0. Выведите эту последовательность в
обратном порядке.
При решении этой задачи нельзя пользоваться
массивами и прочими динамическими структурами данных.
Рекурсия вам поможет.
"""


def reverse():
    n = int(input())
    if n != 0:
        reverse()
    print(n)


reverse()

"""
Возводить в степень можно гораздо быстрее, чем за 𝑛
умножений! Для этого нужно воспользоваться
следующими рекуррентными соотношениями:
𝑎𝑛=(𝑎2)𝑛/2 при четном 𝑛,𝑎𝑛=𝑎⋅𝑎𝑛−1 при нечетном 𝑛.
Реализуйте алгоритм быстрого возведения в степень.
Если вы все сделаете правильно, то сложность вашего алгоритма будет 𝑂(log𝑛).
"""
a = float(input())
n = int(input())


def step_n(a, n):
    if a != 0 and n % 2 == 0:
        return (a ** 2) ** n % 2
    if a != 0 and n % 2 != 0:
        return a * a ** (n - 1)
    else:
        return False


print(step_n(a, n))

"""
Алгоритм Евклида
"""
a = int(input())
b = int(input())


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(a, b))

"""
Ханойские башни
"""

def move(n, x, y):
    if n == 1:
        print("1", x, y)
    else:
        z = 6 - x - y
        move(n-1, x, z)
        print(n, x, y)
        move(n-1, z, y)

n = int(input())
move(n, 1, 3)
