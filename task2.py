# Задайте натуральное число N. Напишите программу, которая составит список простых делителей числа N. (1 - составное число)

number = input ("введите число: ")
def Factor(n):
    list = []
    d = 2
    while d * d <= int(n):
        if n % d == 0:
            list.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        list.append(n)
    return list
print (Factor(int(number)))