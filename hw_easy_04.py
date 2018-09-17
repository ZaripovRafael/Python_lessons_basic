# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random

lst = [random.randint(-100, 100) for _ in range(10)]

print ('список = ', lst)

list_sq = [num**2 for num in lst ]
print(list_sq)

print('\n')

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

# Я не понял как с помощью генератора списков сгенерировать фрукты.

fst_list = ['яблоко', 'ананс', 'яблоко', 'дыня', 'арбуз']
snd_list = ['арбуз', 'виноград', 'персик', 'гранат']
sort_list = list (set (fst_list) & set (snd_list))
print(sort_list)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

list_3 = list(num for num in lst if (num % 3 == 0 and num > 0 and num % 4 != 0) )

print(list_3)
