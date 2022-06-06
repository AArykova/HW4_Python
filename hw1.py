#Создать и заполнить файл случайными целыми значениями. 
#Выполнить сортировку содержимого файла по возрастанию. 

file = 'hw1.txt'

from random import randint
a = -5
b = 100
s = 15
lst = [randint(a, b) for i in range(s)]

with open(file,'w') as f:
    f.write("\n".join(map(str,lst)))
    print(lst)

new_list = []
with open(file,'r') as f:
    new_list = list(map(int, f.readlines()))
    new_list.sort()

with open(file,'w') as f:
    f.write("\n".join(map(str,new_list)))
    print(new_list)
