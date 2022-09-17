'''
                                Вывести матрицу 1
На вход программе подаются два натуральных числа nn и mm, каждое на отдельной строке — количество строк и столбцов в матрице. 
Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке; подряд идут элементы сначала первой строки, затем второй, и т.д.

Напишите программу, которая сначала считывает элементы матрицы один за другим, затем выводит их в виде матрицы.

Формат входных данных
На вход программе подаются два числа n и m — количество строк и столбцов в матрице, далее идут n x m слов, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести считанную матрицу, разделяя ее элементы одним пробелом.
'''


n, m = (int(input()) for _ in range(2))

for row in range(n):
    words = []
    for column in range(m):
        words.append(input())
    print(*words)
