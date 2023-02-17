print("Welcome to the Caesar Cipher")
print("This program encrpts and decrypts text using Caesar Cipher")
print("Student Name: Sanjeev Kumar Sah")
print("Student id: 2329256")

"""Main function that allow users to select between encryption and decryption"""
def main():
    while True:
        mode = input("Select a mode (encrypt/decrypt): ").lower()
        while mode != "encrypt" and mode != "decrypt":
            mode = input("Invalid mode. Select a mode (encrypt/decrypt): ").lower()
        
        """Here user's can enter the message and key to perform the selected operations on the message using the key message"""
        
        message = input("Enter the message: ")
        key = int(input("Enter the key (1-26): "))
        
        """It ask user for their choice between encrypt or decrypt using the key message"""
        
        if mode == "encrypt":
            output = encrypt(message, key)
        else:
            output = decrypt(message, key)
        
        print("Output: " + output)
        
        """Ask user response of y or n if user input is n then program will exist"""
        
        repeat = input("Encrypt/Decrypt another message? (y/n): ").lower()
        while repeat != "y" and repeat != "n":
            repeat = input("Invalid input. Encrypt/Decrypt another message? (y/n): ").lower()
        if repeat == "n":
            break

"""Encrypt function takes two parameters that message and key"""
def encrypt(message, key):
    """It convert the message to uppercase by using .upper() method"""
    message = message.upper()
    """String encrypted will store the encrypted message from the user"""
    encrypted = ""
    """Using a for loop it iterates a message through each character"""
    for char in message:
        """If the character is letter then the function uses ord() and char() to shift the letter by key value"""
        if char.isalpha():
            shifted = chr((ord(char) + key - 65) % 26 + 65)
            """After shifting the letter the shifted letter is added to the encrypted string"""
            encrypted += shifted
        else:
            """If the character is not a letter then it is added to the encrypted string without being shifted"""
            encrypted += char
            """The function return the encrypted message"""
    return encrypted
"""The decrypt function has two parameters that is message and key"""
def decrypt(message, key):
    """Message function convert message to uppercase by using .upper() method"""
    message = message.upper()
    """It store the decrypted message"""
    decrypted = ""
    """By using a for loop the funtion iterates the message through each character"""
    for char in message:
        """If thecharacter is a letter then the function uses the ord() and chr() function to shift the letter by key value"""
        if char.isalpha():
            shifted = chr((ord(char) - key - 65) % 26 + 65)
            """After shifting the letter it is added to the decrypted string"""
            decrypted += shifted
            """If the character is not a letter then it is added to the decrypted string without being shifted"""
        else:
            decrypted += char
            """The function return the decrypted value"""
    return decrypted
"""Main function execute when the program run"""
main()