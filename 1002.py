"""работа с условиями
 2 семинар """

a = int(input()) #Max 2 numb
b = int(input())
if a >= b:
    print(a)
else:
    print(b)


a = int(input())  # Find max number
b = int(input())
c = int(input())

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)


year = int(input())  # Find year //4

if (year % 400 == 0) or (
        year % 4 == 0 and year % 100 != 0):  # Без остатка делится на 400 или делится на 4 без остатка и не делится на 100
    print('Yes')
else:
    print('No')


a = int(input())  # Triangle
b = int(input())
c = int(input())

if a + b > c or a + c > b or b + c > a:
    print('Yes')
else:
    print('No')


a = int(input())  # Count
b = int(input())
c = int(input())
count = 0
if a == b:
    count += 1
    if b == c:
        count += 1
    if a == c:
        count += 1
print(count)


given_number = int(input()) #Ira and Denis
denis_answer = int(input())
ira_answer = int(input())

first_digit = given_number // 1000
second_digit = (given_number // 100) % 10
third_digit = (given_number // 10) % 10
fourth_digit = given_number % 10

is_symmetric = first_digit == fourth_digit and second_digit == third_digit

if is_symmetric == (ira_answer == 1):
    print("Ira solved the problem correctly")
else:
    print("Ira did not solve the problem correctly.")


sq_1 = int(input()) # two squares on a chessboard have the same color
sq_2 = int(input())
col_1 = int(input())
col_2 = int(input())

if (sq_1 + sq_2)%2 == (col_1 + col_2)%2:
    print('YES')
else:
    print('NO')


n = int(input())
m = int(input())
k = int(input())

if (k % n == 0 or k % m == 0) and k <= n * m:
    print('yes')
else:
    print('no')


n = int(input()) #cows
if n >= 11 and n <= 14:
        print(n, 'korov')
else:
        b = n % 10
        if b == 0 or (b >= 5 and b <= 9):
                print(n, 'korov')
        if b == 1:
                print(n, 'korova')
        if b >=2 and b <=4:
                print(n, 'korovy')


a = int(input()) #Triangle ver.2
b = int(input())
c = int(input())

if b <= c or c <= b or c <= a:
        print("impossible")
else:
        if (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2):
            print( "rectangular")
        elif (a ** 2 + b ** 2 < c ** 2) or (a ** 2 + c ** 2 < b ** 2) or (b ** 2 + c ** 2 < a ** 2):
            print("obtuse")
        else:
            print("acute")

