def main():
    vowels = ["a","e","i","o","u"]
    user_input = input("Input: ")
    print ("Output: ", vowel_remover(user_input,vowels))


def vowel_remover(s,vowels):
    no_vowels = ""
    for char in s:
        if not char.lower() in vowels:
            no_vowels = no_vowels + char
    return no_vowels

main()


