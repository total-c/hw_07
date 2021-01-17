# Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’,
# где i это порядковый номер строки в списке.
# Использовать генератор списков.


list_str = [item * 3 for item in 'list']
dict_list_str = [f'{i} - {value}' for i, value in enumerate(list_str)]
print(dict_list_str)
