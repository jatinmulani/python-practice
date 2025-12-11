s = input("Enter a string: ")


if s.startswith(('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')):
    print("The string starts with a vowel.")
else:
    print("The string does NOT end with a consonant.")
consonants = tuple("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

if s.endswith(consonants):
    print("The string ends with a consonant.")

else:
    print("The string does NOT start with a vowel.")
1
