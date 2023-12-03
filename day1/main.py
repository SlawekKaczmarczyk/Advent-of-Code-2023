def get_real_digits(s):
    real_digits = ""
    for char in s:
        if char.isnumeric():
            real_digits += char
    return real_digits

def sum_of_two_digit_nums(plik):
    sum = 0

    with open(plik, 'r') as f:
        for line in f:
            real_digits = get_real_digits(line)

            if len(real_digits) > 1:
                two_digits = int(real_digits[0]) * 10 + int(real_digits[-1])
                sum += two_digits
            elif len(real_digits) == 1:
                sum += int(real_digits) * 11

    return sum

input_file = 'input.txt'
result = sum_of_two_digit_nums(input_file)
print("Wynik to:", result)
