# TODO Найдите количество книг, которое можно разместить на дискете
information_volume = 1.44   # Информационный объем дискеты в Мб
number_of_pages = 100   # Количество страниц в книге
number_of_lines = 50    # Количество строк на странице
number_of_characters= 25    # Количество символов к строке
information_for_1_character = 4 # Информационный объем 1 символа в байтах
one_book = ((number_of_pages * number_of_lines * number_of_characters * information_for_1_character) / 1024)/1024 # Размер 1 книги в Мб
the_number_of_books_on_the_floppy_disk = round(information_volume // one_book) # Искомое значение
print("Количество книг, помещающихся на дискету:", the_number_of_books_on_the_floppy_disk)
