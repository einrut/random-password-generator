import random
import string

length = int(input("Enter your desired password length: "))


while True:
    print("Use lowercase, uppercase, or both?")
    choice = input().lower()

    lower = upper = False
    if choice == "both":
        lower = upper = True
        break
    elif choice == "lower":
            lower = True
            break
    elif choice == "upper":
            upper = True
            break
    else:
        print("Invalid input, try again.")


numbers = input("Use numbers? (Y/N): ").lower() == "y", "yes"
specialChar = input("Use special characters? (Y/N): ").lower() == "y", "yes"


characters = ""
if lower:
    characters += string.ascii_lowercase
if upper:
    characters += string.ascii_uppercase
if numbers:
    characters += string.digits
if specialChar:
    characters += string.punctuation

password = ''.join(random.choice(characters) for _ in range(length))

print("Here's your password!")
print(password)
