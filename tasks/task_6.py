chars: str = input("Введите строку: ")

# Перевод строки в кортеж и отбрасывание не уникальных символов
set_chars: set = set(chars)

# Вычисление количества уникальных символов
len_chars: int = len(set_chars)

print(
    "Уникальные символы:", tuple(set_chars),
    "\nКоличество уникальных символов:", len_chars
)

# print(('a', 'b', 'c', 'd', 'e', 'f'))
# print(['a', 'b', 'c', 'd', 'e', 'f'])
# print({'a', 'b', 'c', 'd', 'e', 'f'})
