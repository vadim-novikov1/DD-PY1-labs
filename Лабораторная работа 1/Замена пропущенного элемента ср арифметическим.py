numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
numbers_2 = numbers[4] # Вычленяем None
numbers_1 = sum(numbers[0:4]) + sum(numbers[5:]) # Сумма без None
numbers_3 = numbers_1 / (len(numbers)) # Среднее врифметическое ряда без None
numbers_2 = numbers_3 # Присваиваем None зачение ср арифметического
numbers[4] = numbers_2 # Возвращаем обновленное значение None в ряд
print("Измененный список:", numbers)

