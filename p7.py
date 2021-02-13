"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Рекурсия вам нужна для решения левой части выражения.
Полученный результат нужно просто сравнить с результатом в правой.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Подсказка:
В ф-цию принимаются два элемент - это левая и правая части

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def proof_of_equality(n, final_number, right_side):
    if n == 0:
        return f"Proof of equality {final_number} = {right_side * (right_side + 1) / 2}"
    else:
        final_number += n
        print(final_number)
    return proof_of_equality(n - 1, final_number, right_side)  # храним в right_side введённое значение для
    # вычислений правой стороны выражения, так как переменную n используем для счётчика и суммирования


try:
    numb = int(input("Input the number: "))
except ValueError:
    print("Wrong input for number! Try again")
else:
    print(proof_of_equality(numb, 0, numb))
