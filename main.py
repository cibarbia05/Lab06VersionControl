def encoder(password):  # Christian Ibarbia Ruiz
    return ''.join([str((int(digit) + 3)) for digit in password])


def decoder(password):  # Joseph Guzman
    decoded_password = ''
    for i in password:
        decoded_password += str(int(i) - 3)
    return decoded_password


if __name__ == '__main__':  # main method
    print("Menu\n"
          "-------------\n"
          "1. Encode\n"
          "2. Decode\n"
          "3. Quit")

    option = int(input("\nPlease enter an option: "))
    encoded_password = ''

    while option != 3:  # loops while user has not selected 3 as an option
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encoder(password)
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            decoded_password = decoder(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.\n")
        elif option == 3:
            break
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit\n")
        option = int(input("Please enter an option: "))
