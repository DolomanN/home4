# Вычислить число c заданной точностью d
# Пример:
# - при d = 3, π = 3.141

n = input ("Введите точность вычисления числа ПИ: ")
x = 0
for i in range(1, 1000000):
    x = x+4*((-1)**(i+1))/(2*i-1)
print(round(x, int(n)))