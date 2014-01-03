
p = 23
q = 29
# 2 ** 12
n = p * q
o = (p - 1) * (q - 1)
e = 15
d = 41
#o = 616
# ed = 1(mod o)

letters = "abcdefghijklmnopqrstuvwxyz"

#c = m^e(mod n)
#m = e^d(mod n)    

def letter_to_number(letter):
    number = 0
    exp = 0
    encrypt = 0
    for i in range(0, len(letters)):
        if letter == letters[i]:
            number = i

    exp = number ** d
    encrypt = exp % n
    print (encrypt)
    encrypt = bin(encrypt)
    return encrypt

def encrypt(text):
    encrypted_message = []
    for i in range(0, len(text)):
        encrypted_message.append(letter_to_number(text[i]))

    return encrypted_message

def number_to_letter(num):
    letter = ""
    encrypt = int(num, 2)
    exp = encrypt ** e
    mes = exp % n
    print(mes)
    letter = letters[mes]
    return letter

def decrypt(encrypt):
    decrypted_message = ""
    for i in range(0, len(encrypt)):
        decrypted_message = decrypted_message + number_to_letter(encrypt[i])
        
    print(decrypted_message)
    return decrypted_message

def main():
    message = "hi"
    enc_mes = []
    enc_mes = encrypt(message)
    print(enc_mes)
    print(enc_mes[0])

    test = ""
    test = decrypt(enc_mes)
    print(test)

    

if __name__ == '__main__':
    main()

    
