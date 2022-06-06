# Дан список чисел. Создать список в который попадают числа, 
# описывающие возрастающую последовательность и содержащие максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#  [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
#  Порядок элементов менять нельзя
     
kol = int(input('Введите количество элементов - '))

list = []

for i in range(0, kol):
    temp = int(input(f'Введите {i} элемент - '))
    list.append(temp)
print(list)

def sort(list):
     new_list = []
     for i in range(len(list)):
         if list[i] == max(list[:i+1:]) and list[i] not in new_list:
             new_list.append(list[i])
     return new_list

print(sort(list))
2