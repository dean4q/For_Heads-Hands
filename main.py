import random


def massiv_gen(n):
    '''
    Функция для создания и сортировки массивов из тестового задания
    :param n:
    :return:
    '''
    array = []
    size_of_subarray = set()     #зв этом множествебудут храниться n-чисел,которые не будут повторяться
    while len(size_of_subarray) < n:
        size_of_subarray.add(int(random.random() * 10))   #заполняем множество

    for i, size in enumerate(size_of_subarray): #значение елемента множества соответствует размену вложенного массива
        sub_array = [int(random.random() * 100) for _ in range(size)]
        array.append(sub_array)
    for number_array in range(len(array)): #сортировка
        if number_array % 2 == 0:
            array[number_array] = sorted(array[number_array])
        else:
            array[number_array] = sorted(array[number_array], reverse=True)
    return array




