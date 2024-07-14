alphabet =['a', 'b', 'c', 'd', 'e', 'f',
           'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y' , 'z']

def encryption(plain_text,shift_key):
 cipher_text=""

 for char in plain_text:
  position = alphabet.index(char)
  new_position = (position+shift_key)%26
  cipher_text += alphabet[new_position]

 print(f"Encrypted Message :{cipher_text}")

def decryption(cipher_text,shift_key):
 plain_text=""

 for char in cipher_text:
    position = alphabet.index(char)
    new_position =(position-shift_key)%26
    plain_text += alphabet[new_position]

 print(f"Decrypted Message : {plain_text} ")




choice =input("Encryption 'Encrypt' or Decryption 'Decrypt': \n")
text = input("Enter the text you want to encrypt \n")
shift = int(input("Enter you shift key \n"))

if choice == "Encrypt":
    encryption(plain_text=text,shift_key=shift)

elif choice == "Decrypt":
     decryption(cipher_text=text,shift_key=shift)