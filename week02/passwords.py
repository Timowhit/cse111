# Password Strength Tester
# Author: Timothy Whitehead
# added a file validator, checking to see if you have the necessary files to check against common passwords
LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

def word_in_file(word, filename):
    common = False
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                if word == line.strip():
                    common = True
                    break
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Skipping common password check against {filename}.")
        pass
    if common:
        score = 0
        print("This password is too common. Please choose a different password.")

def word_has_character(word, character_list):
    character_list = [LOWER, UPPER, DIGITS, SPECIAL]        
    for char in word:
        if char in character_list:
            return True
    return False

def word_complexity(word):
    has_lower = any(char in LOWER for char in word)
    has_upper = any(char in UPPER for char in word)
    has_digit = any(char in DIGITS for char in word)
    has_special = any(char in SPECIAL for char in word)

    score = 0

    if has_lower:
        score += 1
    if has_upper:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1
    if score > 5:
        score = 5
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength

def password_strength(password, min_length, strong_length):
    min_length = 10
    strong_length = 16
    length = len(password)
    score = 0

    if length < min_length:
        print(f"Password is too short. It should be at least {min_length} characters long.")
        return 0
    elif length >= strong_length:
        print("Password is long, length trumps complexity. This is a very good password.")
        score = 5
    elif length >= min_length:
        score += 1

    word_in_file(password, "toppasswords.txt")
    word_in_file(password, "wordlist.txt")

    return score
    
def main():
    while True:
        password = input("Enter a password: ")
        score = password_strength(password, 10, 16)

        complexity = word_complexity(password)

        print(f"Password Strength Score: {score}")

        save_choice = input("Type 'save' to save this password, type 'quit' to exit, or press enter/type anything else to test another password: ")

        if save_choice.lower() == "save":
            print("Password saved. Quitting password strength tester.")
            break
        if save_choice.lower() == "quit":
            print("Quitting password strength tester.")
            break

        print("-"*40)

if __name__ == "__main__":
    main()
