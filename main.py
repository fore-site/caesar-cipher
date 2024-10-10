alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']

# define the caesar function
def caesar(cipher_text, shift_amount, command):
    solved_text = ''

    # if user enters a shift greater than number of letters in alphabets, use modular arithmetic
    shift_amount %= 26
    if command == 'decode':
        shift_amount *= -1
    for letter in cipher_text:
        if letter not in alphabets:
            solved_text += letter
        else:
            solved_text += alphabets[alphabets.index(letter) + shift_amount]
    return solved_text

# main function for user interaction
def main():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    # error handling if user types anything other than 'decode' or 'encode'
    while direction != 'encode' and direction != 'decode':
        direction = input("Please enter a valid command. Type 'encode' to encrypt or 'decode' to decrypt\n")
        if direction == 'encode' or direction == 'decode':
            break

    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))

    if direction == 'encode':
        print(f'The encoded text is {caesar(text, shift, direction)}')
    elif direction == 'decode':
        print(f'The decoded text is {caesar(text, shift, direction)}')

main()
# allow user restart or quit the program
while True:
    start_over = input("Type 'yes' if you want to go again, otherwise type 'no':\n").lower()
    if start_over == 'yes':
        main()
    elif start_over == 'no':
        break
    else:
        continue