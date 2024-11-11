import random
import string

def generatePassword(length):
    # Define the character sets to use in generating the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    # Prompt the user to specify the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive number for the length.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Generate the password
    password = generatePassword(length)

    # Display the password
    print("Generated password:", password)

if __name__ == "__main__":
    main()
     
