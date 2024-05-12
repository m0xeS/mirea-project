def convert_to_integer(char):
    if char.isdigit():
        return int(char)
    else:
        return None  # Возвращаем None, если переданная переменная не является цифрой

input_char = input("Введите символ: ")
result = convert_to_integer(input_char)
if result is not None:
    print("Результат:", result)
else:
    print("Введенный символ не является цифрой.")
