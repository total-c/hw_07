# Описать функцию fact2(n), вычисляющую двойной факториал: n!! = 1·3·5·...·n,
# если n — нечетное;
# n!! = 2·4·6·...·n, если n — четное (n > 0 — параметр целого типа).
# С помощью этой функции найти двойные факториалы пяти случайных целых чисел.

import random

def fact2(n: int) -> int:
    """Функция fact2 расчитывает двойной фактириал полученного значения"""
    factorial = 1
    if not n % 2:
        for i in range(2, n+1, 2):
            factorial = factorial * i
        return factorial
    elif n % 2:
        for i in range(1, n+1, 2):
            factorial = factorial * i
        return factorial

def main():
    """Функция main генерирует 5 случайных чисел и передает их в переменную n.
    Предназначена для тестирования функции fact2"""
    list_random = []
    for i in range(5):
        list_random.append(random.randint(1, 20))
    for i in list_random:
        n = i
        print(fact2(n))

if __name__ == '__main__':
    main()
