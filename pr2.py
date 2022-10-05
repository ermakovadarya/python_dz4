# задача 2 . Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random

sp=[random.randint(0,10) for _ in range(10)]
print(sp)
res=[]
def new_sp(res):
    res.append(sp[0])
    for i in sp:
        fl=True
        for j in res:
            if i==j:
                fl=False
        if fl:
            res.append(i)
                

new_sp(res)
print(res)