def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[:1])
    if len(str_number) == 1:
        return first
    if len(str_number) > 0:
        return first * get_multiplied_digits(int(str_number[1:]))

print(get_multiplied_digits(4564))

