'''
Составить алгоритм: на входе есть числовой массив, необходимо вывести элементы массива кратные 3
'''
lst = [int(x) for x in input().split()]
for i in range(len(lst)):
    if lst[i] % 3 == 0:
        print(lst[i], end=' ')