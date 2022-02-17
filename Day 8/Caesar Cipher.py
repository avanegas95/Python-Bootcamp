from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
redo = True
print(logo)

def caesar(input, shift_amount, dir):
    word = ""
    shift_amount = shift_amount % 26
    if dir == "decode":
        shift_amount = shift_amount * -1
    for i in input:
        if i not in alphabet:
            word += i
        else:
            word += alphabet[alphabet.index(i) + shift_amount]       
    print(f"The {direction}d word is {word}")
    
while redo:    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(input=text, shift_amount=shift, dir=direction)

    user_continue = input("Type 'yes' if you would like to go again. Otherwise type 'no'\n").lower()
    if user_continue == 'no':
        redo = False
        print("Goodbye!")