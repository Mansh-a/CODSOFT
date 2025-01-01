import random
import string

def get_complexity():
    """Prompt the user to select password complexity until a valid choice is entered."""
    while True:
        print("\nChoose the complexity level for your password:")
        print("1. Only letters")
        print("2. Letters and numbers")
        print("3. Letters, numbers, and special characters")
        try:
            complexity = int(input("Enter your choice (1-3): "))
            if complexity in [1, 2, 3]:
                return complexity
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")

def get_password_length():
    """Prompt the user to specify password length until a valid input is provided."""
    while True:
        try:
            length = int(input("\nEnter the desired length for your password (minimum 6 characters): "))
            if length >= 6:
                return length
            else:
                print("Password length should be at least 6 characters. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def generate_password():
    """Main function to handle password generation and menu navigation."""
    while True:
        print("\nWelcome to the Password Generator!")
        print("Choose an option:")
        print("1. Generate a password")
        print("2. Help (How to use this tool)")
        print("3. Exit")
        try:
            choice = int(input("Enter your choice (1-3): "))
            
            if choice == 1:
                # Get password length
                length = get_password_length()
                
                # Get password complexity
                complexity = get_complexity()
                
                # Define character sets based on complexity
                if complexity == 1:
                    characters = string.ascii_letters
                elif complexity == 2:
                    characters = string.ascii_letters + string.digits
                elif complexity == 3:
                    characters = string.ascii_letters + string.digits + string.punctuation
                
                # Generate the password
                password = ''.join(random.choice(characters) for _ in range(length))
                
                # Display the password
                print(f"\nYour generated password is: {password}")
            
            elif choice == 2:
                print("\nHelp Section:")
                print("1. Choose 'Generate a password' to create a strong password.")
                print("2. Follow the prompts to enter the desired length and complexity.")
                print("3. Exit the tool anytime by selecting option 3.")
            
            elif choice == 3:
                print("Exiting the Password Generator. Goodbye!")
                break
            
            else:
                print("Invalid choice. Please select a valid option from the menu.")
        
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the menu options.")

if __name__ == "__main__":
    generate_password()
