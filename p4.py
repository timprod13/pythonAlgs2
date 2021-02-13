"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак
"""


def my_addition(n, final_number, start_number):
    if n == 0:
        return f"Their addition is {str(final_number)}"
    else:
        start_number = -(start_number / 2)  # так как изначально задал -2 - делаем по условию (1, -0.5, 0.25...)
        final_number += start_number  # производим операцию сложения
    return my_addition(n - 1, final_number, start_number)  # вместо счётчика у нас количество элементов


try:
    numb = int(input("Input number of elements: "))
except ValueError:
    print("Wrong input! Try again")
else:
    print(f"Amount of elements is {str(numb)}")     # так как при рекурсии вводимое количество мы испортили,
    # то выводим его отдельно
    print(my_addition(numb, 0.0, -2.0))
