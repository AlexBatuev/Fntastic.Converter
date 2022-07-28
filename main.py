
# Цель - конвертировать исходную строку, в новую строку, где каждый символ заменяется на символ “ ( ”,
# если символ встречается только один раз или на “ ) “, если символ встречается больше одного раза.
# При решении программа должна игнорировать заглавные буквы,
# при определении дубликатов (т.е. “А” и “а” - это один и тот же символ).
# Пример входных и выходных данных:
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("


def convert_string(incoming_string: str) -> str:

    incoming_string = incoming_string.lower()

    founded = {}
    for o in incoming_string:
        if o in founded:
            founded[o] += 1
        else:
            founded[o] = 1

    for f in founded:
        if founded[f] == 1:
            incoming_string = incoming_string.replace(f, '(')
        else:
            incoming_string = incoming_string.replace(f, ')')

    return incoming_string


if __name__ == '__main__':
    input_string = input('Пожалуйста, введите строку для конвертации:\n')
    print(convert_string(input_string))
