# задача 3. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

# *Пример:* 

# # - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
def save(k):
    with open('text.txt', 'a') as fh:  
        fh.write(k)

k=random.randint(1,10)
sp=[random.randint(0,100) for _ in range(k+1)]
print(sp)
save(f'Многочлен степени {k}\n')

def polynomial(k,sp):
    if sp[0]==0:
        save('Старший коэффициент = 0, многочлен не существует')
        return
    for i in range(0,len(sp)-1):
        if sp[i]!=0 and i!=len(sp):
            save(f'{sp[i]} * x **{k} + ')
        k-=1
    save(f'{sp[i+1]} = 0\n')

polynomial(k,sp)
print('Задача выполнена')



# def load():
#             # загрузить из json
#             fname='BD.json' #открываем файл
#             with open(fname, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
#                 BD = json.load(fh)  # загружаем из файла данные в словарь data
#             print('БД успещно загружена')
#             return BD

  
        
