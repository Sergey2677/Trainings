# Вводится список из целых чисел в одну строчку через пробел.
# Необходимо выполнить его сортировку по возрастанию с помощью алгоритма сортировки слиянием.
# Функция должна возвращать новый отсортированный список.
# Вызовите результирующую функцию сортировки для введенного списка и отобразите результат на экран в виде последовательности чисел,
# записанных через пробел.
# Подсказка. Для разбиения списка и его последующей сборки используйте рекурсивные функции.
# P. S. Теория сортировки в видео предыдущего шага.
# Sample Input:
# 8 11 -6 3 0 1 1
# Sample Output:
# -6 0 1 1 3 8 11

# put your python code here

lst = list(map(int, input().split()))


def merge_two_lists(first_lst, second_lst):
    F = len(first_lst)
    S = len(second_lst)
    merged_list = []
    i = 0
    j = 0
    while (i < F) and (j < S):
        if first_lst[i] > second_lst[j]:
            merged_list.append(second_lst[j])
            j += 1
        else:
            merged_list.append(first_lst[i])
            i += 1
    merged_list += first_lst[i:] + second_lst[j:]
    return merged_list

def split_and_merge_list(lst):
    mid = len(lst) // 2
    righthalf = lst[:mid]     # деление массива на два примерно равной длины
    lefthalf = lst[mid:]

    if len(righthalf) > 1: # если длина 1-го списка больше 1, то делим дальше
        righthalf = split_and_merge_list(righthalf)
    if len(lefthalf) > 1: # если длина 2-го списка больше 1, то делим дальше
        lefthalf = split_and_merge_list(lefthalf)

    return merge_two_lists(righthalf, lefthalf)   # слияние двух отсортированных списков в один

print(*split_and_merge_list(lst))
