def encoder(password):
    return ''.join([str((int(digit) + 3)) for digit in password])


if __name__ == '__main__':
    print("Menu\n"
          "-------------\n"
          "1. Encode\n"
          "2. Decode\n"
          "3. Quit")

    option = int(input("\nPlease enter an option: "))
    encoded_password = ''

    while option != 3:
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encoder(password)
            print("Your password has been encoded and stored!")
        elif option == 2:
            decoded_password = decoder(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
        elif option == 3:
            break
        option = int(input("Please enter an option: "))


