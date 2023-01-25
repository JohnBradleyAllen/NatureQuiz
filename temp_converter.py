def c_2_f(celsius):
    return int((celsius * 9/5) + 32)


def f_2_c(fahrenheit):
    return int((fahrenheit - 32) * 5/9)


def main():
    print()
    celsius_to_convert = int(
        input("Enter the C temperature to convert to F: "))
    celsius = convert.c_2_f(celsius_to_convert)
    print(celsius_to_convert, celsius)
    print()
    fahrenheit_to_convert = int(input('Enter the F temp to convert to C: '))
    fahrenheit = convert.f_2_c(fahrenheit_to_convert)
    print(fahrenheit_to_convert, fahrenheit)
