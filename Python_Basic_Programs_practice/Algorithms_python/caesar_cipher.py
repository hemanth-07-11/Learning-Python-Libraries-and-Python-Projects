from string import ascii_letters

def encrypt(input_string: str, key: int, alphabet=None) -> str:

    alpha = alphabet or ascii_letters

    result = ""

    for character in input_string:
        if character not in alpha:
        
            result += character
        else:
            new_key = (alpha.index(character) + key) % len(alpha)

            result += alpha[new_key]

    return result

def decrypt(input_string: str, key: int, alphabet=None) -> str:
  
    key *= -1

    return encrypt(input_string, key, alphabet)

def brute_force(input_string: str, alphabet=None) -> dict:
    alpha = alphabet or ascii_letters

    key = 1

    result = ""

    brute_force_data = {}

    while key <= len(alpha):

        result = decrypt(input_string, key, alpha)

        brute_force_data[key] = result

        result = ""
        key += 1

    return brute_force_data


def main():
    while True:
        print(f'\n{"-" * 10}\n Menu\n{"-" * 10}')
        print(*["1.Encrpyt", "2.Decrypt", "3.BruteForce", "4.Quit"], sep="\n")

        choice = input("\nWhat would you like to do?: ").strip() or "4"

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice, please enter a valid choice")
        elif choice == "1":
            input_string = input("enter the string to be encrypted: ")
            key = int(input("enter off-set: ").strip())

            print(encrypt(input_string, key))
        elif choice == "2":
            input_string = input("enter the string to be decrypted: ")
            key = int(input("enter off-set: ").strip())

            print(decrypt(input_string, key))
        elif choice == "3":
            input_string = input("enter the string to be decrypted: ")
            brute_force_data = brute_force(input_string)

            for key, value in brute_force_data.items():
                print(f"Key: {key} | Message: {value}")

        elif choice == "4":
            print("Thank You")
            break


if __name__ == "__main__":
    main()
