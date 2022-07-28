# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и вывести на экран.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint

k = int(input("Введите натуральную степень: "))

numbers = []

for i in range(int(k)):
    numbers.append(randint(0, 100))

print (numbers)

func = ("")

#for i in range(int(k)):
for i in numbers:
    func = func + (str(f"{i}**{k} + "))
    k = k - 1
remove = func[:len(func)-2]
print(f"{remove} = 0" )


#не очень понял суть задания, и не силен в математике, сделал как мог) 