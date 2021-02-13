"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Подсказка:
Базовый случай здесь - угадали число или закончились попытки
"""
from random import randint


def my_guess(n, attempts, hidden_number):
    if attempts == 0:
        return f"You lose! Hidden number is {str(hidden_number)}"
    try:
        n = int(input(f"You've got only {attempts} attempt(s)! Input number from 0 to 100: "))
        if n == hidden_number:
            return f"Congratulations! Hidden number is {str(hidden_number)}! You took only {str(11 - attempts)} " \
                   f"attempts to win "
        else:
            print("You didn't guess, Try again")
    except ValueError:
        print("Wrong input! Try again")
    return my_guess(n, attempts - 1, hidden_number)


input("Guess game! Press Enter to begin!")
print(my_guess(101, 10, randint(0, 100)))       # перенёс input в функцию, чтобы корректно засчитывать неправильный
# ввод за попытку, для этого пришлось ещё до ввода пользователем числа передать 101, чтобы точно не попасть в
# диапазон рандома
