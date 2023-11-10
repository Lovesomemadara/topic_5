chars: str = input("Введите строку: ")

# Преобразование списка в кортеж и удаление повторяющихся символов
set_chars: set = set(chars)

# Преобразование кортежа в множество
ref_chars: list = list(set_chars)

print(f"Уникальные символы: {ref_chars}")
