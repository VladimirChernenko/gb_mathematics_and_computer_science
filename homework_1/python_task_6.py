"""
Описать блок-схему перевода десятичного представления числа в двоичное.
"""

def main(number):
    list_x = []
    while number > 1:
        list_x.append(str(number%2))
        number //= 2
    list_x.append(str(number))
    list_x.reverse()
    return ''.join(list_x)

if __name__ == '__main__':
    print(main(16))