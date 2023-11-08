student_info = {
    "name": "Анна",
    "age": 20,
    "group_number": "А101"
}

# Выявление ключей из словаря
keys_set = dict.keys(student_info)

# Преобразование списка в множество
ref_set = set(keys_set)

print(ref_set)
