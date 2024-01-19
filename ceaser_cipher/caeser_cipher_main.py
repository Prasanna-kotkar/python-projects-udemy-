# Caesar cipher converter

import art

print(art.logo)

def cipher(t,s,d):
    text = ""
    for i in t:
        if i in alphabet:
            x = alphabet.index(i)
            if d == "encode":
                new_x = (x + s) % 26
            elif d == "decode":
                new_x = x - s
            new_letter = alphabet[new_x]
            text += new_letter
        else:
            text += i
    print(f"The {d}d text is: {text}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    cipher(t = text,s = shift,d = direction)
    ans = input('Type "yes" to continue or "no" to stop:\n').lower()
    if ans == "no":
        print("!!! GOODBYE. !!!")
        break
