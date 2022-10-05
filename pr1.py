# задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n=int(input('Введите число '))
sp=[]
def mult (n):
    global sp
    k=2
    while n>1:
        if n%k==0:
            sp.append(k)
            n=n/k
            k=2
        else:
            k+=1

mult(n)
print(sp)