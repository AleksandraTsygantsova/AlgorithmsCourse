# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
# Работает с русским алфавитом.

alph = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м',
        'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы','ь', 'э', 'ю', 'я']

num = int(input('Введите число: '))
print(f'Буква в алфавите под номером {num}: {alph[num-1]}')
