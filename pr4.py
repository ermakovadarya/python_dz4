# задача 4. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

x=int(input('Введите первое число '))
y=int(input('Введите второе число '))

def NOK(x,y):
    if x>y:
        max=x
    else:
        max=y
    while True:
        if max%x==0 and max%y==0:
            return max
        max+=1

print('НОК= ', NOK(x,y))