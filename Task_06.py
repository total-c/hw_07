# Создать lambda функцию, которая принимает на вход неопределенное количество
# именных аргументов и выводит словарь с ключами удвоенной длины.
# {‘abc’: 5} -> {‘abcabc’: 5}

func = ((lambda **kwargs: {key*2: val for key, val in kwargs.items()})(abc = 3, dfg = 4, age = 33))
print(func)
