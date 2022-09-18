
# TASK 1
#x = int(input("Введите число:"))
#for i in range(1, x+1):
   # print(int(math.pow(i, 3)))

# TASK 2
#A = input("введите что-то").split()
#A.reverse()
#print(A)

# TASK 3
#x = int(input("Введите число: "))
#f = 1
#while x > 1:
#    f = x * f
#    x = x - 1
#print(f)

# TASK 4
#x = int(input("Введите число: "))
#f = 1
#while x > 1:
#    f = x + f
#    x = x - 1
#print(f)

# TASK 5

# def getPalindrom(text):
#     if text == text[::-1]:
#         return True
#     return False
#
# print(getPalindrom(input("Введите что-нибудь: ")))

# TASK 6
#
# R = int(input('Введите кол-во строк: '))
# for i in range(0, R + 1):
#     for j in range(R - i, 0, -1):
#         print(j, end=' ')
#     print()

# TASK 7

# R = int(input('Введите кол-во строк: '))
# for i in range(R+1):
#     for j in range(i):
#         print(i, end=' ')
#     print('')

# TASK 8

# get_Discount = lambda d,s: d-(d/100*s)
# sum = get_Discount(*map(int,input("Введите числа: ").split()))
# print(sum)


# TASK 9

# def sum(n):
#     if n == 0:
#         return 0
#     else:
#         return n+sum(n-1)
# print(sum(int(input("Введи число: "))))


# TASK 10
pifagor = lambda a,b,c: a*a+b*b==c
sum = pifagor(*map(int,input("Введите числа: ").split()))
print(sum)


