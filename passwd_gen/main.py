
import string # for character sets
import secrets # for cryptographic security 
import random


# print(secrets.choice(string.digits)) # Liefert nicht-deterministische, nicht vorhersagbare Zufallswerte.
# print(random.choice(string.digits)) # Dieser ist deterministisch: Wenn man den Seed kennt, kann man alle folgenden Werte vorhersagen.


def check_upper(passwd):
    for char in passwd:
        if (char.isupper()): # in string.ascii_uppercase
            return True
    return False  

def check_special(passwd):
    for char in passwd:
        if (char in string.punctuation):
            return True
    return False    

def generate_pw(lenght, containUpper, containSpecial):

    if lenght < 3:
        raise ValueError("a password must be longer than 8 characters !")
    
    upper_caracter = string.ascii_uppercase
    lower_caracter = string.ascii_lowercase
    digits = string.digits
    symbole = string.punctuation

    caracter_pool = lower_caracter + digits

    if (containUpper): caracter_pool += upper_caracter
    if (containSpecial): caracter_pool += symbole

    generated_pass = ''

    for _ in range(lenght):
        generated_pass += secrets.choice(caracter_pool)

    if(containUpper == check_upper(generated_pass) and containSpecial == check_special(generated_pass)):
        return generated_pass 
    else:
        return generate_pw(lenght, containUpper, containSpecial)


if __name__ == '__main__':

    result = generate_pw(3,True,True)
    print(f'generated password: {result}')
    print(f'contain Uppercases: {check_upper(result)}')
    print(f'contain Symboles: {check_special(result)}')