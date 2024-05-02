import time
import random
import sys

def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr(((ord(char) - 65) + shift) % 26 + 65)
            else:
                encrypted_text += chr(((ord(char) - 97) + shift) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def encrypt_message():
    print("\nEncrypt your confidential message")
    message = input("Enter the message to encrypt: ")
    shift = int(input("Enter the encryption key (an integer value): "))
    encrypted_message = caesar_cipher(message, shift)
    print("Encrypted message:", encrypted_message)

def decrypt_message():
    print("\nDecrypt your encrypted message")
    message = input("Enter the encrypted text: ")
    shift = int(input("Enter the decryption key (an integer value): "))
    decrypted_message = caesar_cipher(message, -shift)
    print("Decrypted message:", decrypted_message)

def exit_program():
    print("\nExiting the secure messaging system.")
    print("Goodbye!")
    sys.exit()

def default_action():
    print("\nInvalid choice. Please try again.\n")

options = {
    "1": encrypt_message,
    "2": decrypt_message,
    "3": exit_program
}

def start_messaging_system():
    print("SECURE MESSAGE ENCRYPTION SYSTEM")
    print("DESIGNED BY A PASSIONATE DEVELOPER\n")
    print("1: ENCRYPT MESSAGE")
    print("2: DECRYPT MESSAGE")
    print("3: EXIT\n")

    while True:
        choice = input("What do you want to do? Please enter the option number: ")
        options.get(choice, default_action)()

if __name__ == "__main__":
    start_messaging_system()