fruits = dict({
    ('яблоко', 50), ('банан', 30), ('груша', 40), ('апельсин', 35)
})

print("Список фруктов и их цены:")
print(fruits, "\n")

user_input = input("Выберите фрукт из списка: ")

# Выявление стоимости фрукта по вписанному ключу пользователем
price = fruits[user_input]

print(f"Цена {user_input} - {price}")
