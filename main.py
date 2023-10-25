def encoder(password):
    return ''.join([str((int(digit) + 3)) for digit in password])


if __name__ == '__main__':
    print(encoder('00009962'))
