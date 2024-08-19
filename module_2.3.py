# Записываем исходный список в переменную my_list
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

# Инициализируем переменную для отслеживания текущего индекса
current_index = 0

# Начинаем цикл с первого элемента списка
while current_index < len(my_list):
    # Проверяем, является ли текущее число положительным
    if my_list[current_index] > 0:
        # Выводим положительное число
        print(my_list[current_index])
        # Переходим к следующему элементу
        current_index += 1
    else:
        # Если число отрицательное или ноль, пропускаем его и продолжаем цикл
        current_index += 1
        continue

# Выводим сообщение, если список закончился, но не было найдено отрицательных чисел
print("Все числа положительные!")