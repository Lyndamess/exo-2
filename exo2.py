def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)


def has_up(s):
    return any(char.isupper() for char in s)


def has_lower(s):
    return any(char.islower() for char in s)


def has_special(s):
    special_characters = "\"!@  # $%^&*()-+?_=,<>/\""
    return any(char in special_characters for char in s)


s = input("saisir passeword")

if not (10 <= len(s) <= 25):
    print("taille invalid")

elif not has_numbers(s):
    print("mode de passe ne contain pas de numero")
elif not has_special(s):
    print("mode de passe ne contain pas de caractere specified")

elif not has_up(s):
    print("mode de passe ne contain pas de majuscule")

elif not has_lower(s):
    print("mode de passe ne contain pas de majuscule")
