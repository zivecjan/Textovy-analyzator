"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jan Živec
email: zivecjan@seznam.cz
discord: honzaz._21516
"""

import re
from TEXTS import TEXTS

delimiter = ("-" * 40)

username = input("username: ")
password = input("password: ")

"""
Seznam registrovaných uživatelů s jejich hesly:
"""
user_password = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

print(delimiter)

def analyze_text(text_list):
    """
    Cílem funkce je analyzovat vybraný text z vybraného seznamu textů.
    Funkce nejprve přivítá uživatele, požádá ho o vstup ve formě čísla textu z vybraného rozsahu textů, ověří, zda uživatel zadal vstup ve formátu čísla.
    Pokud je vstup číslo a toto číslo je v seznamu textů, funkce vybraný text postupně analyzuje.
    """
    print(f"Welcome to the app, {username}\nWe have {len(text_list)} texts to be analyzed.")

    print(delimiter)        

    text_number = input(f"Enter a number between 1-{len(text_list)} to select: ")

    print(delimiter)   

    text = None

    if text_number.isnumeric():
        text_number = int(text_number)
        if 1 <= text_number <= len(text_list):
            text = text_list[text_number - 1]

            """
            Rozdělení textu na slova a vypsání celkového počtu slov:
            """
            word_count = len(text.split())
            print(f"There are {word_count} words in the selected text.")

            """
            Pro každé slovo, které začíná velkým písmenem, započítej do proměnné words_with_cap hodnotu +1.
            Po projití celého textu se vypíše jejich celkový počet v textu:
            """
            words_with_cap = 0
            for word in text.split():
                if word[0].isupper() is True:
                    words_with_cap += 1
                else:
                    continue
            print(f"There are {words_with_cap} titlecase words.")

            """
            Pro každé slovo, které je psané velkými písmeny a zároveň se jedná pouze o alfanumerické hodnoty, započítej do proměnné words_in_uppercase hodnotu +1.
            Po projití celého textu se vypíše jejich celkový počet v textu:
            """
            words_in_uppercase = 0
            for word in text.split():
                if word.isupper() is True and word.isalpha() is True:
                    words_in_uppercase += 1
                else:
                    continue
            print(f"There are {words_in_uppercase} uppercase words.")

            """
            Pro každé slovo, které je psané malými písmeny a zároveň se jedná pouze o alfanumerické hodnoty, započítej do proměnné words_in_lowercase hodnotu +1.
            Po projití celého textu se vypíše jejich celkový počet v textu:
            """
            words_in_lowercase = 0
            for word in text.split():
                if word.islower() is True and word.isalpha() is True:
                    words_in_lowercase += 1
                else:
                    continue
            print(f"There are {words_in_lowercase} lowercase words.")

            """
            Pro každé číslo v textu započítej do proměnné numbers hodnotu +1.
            Po projití celého textu se vypíše celkový počet čísel v textu.
            Následně se vypíše také jejich suma:
            """
            numbers = 0
            numbers_sum = 0
            for word in text.split():
                if word.isnumeric() is True:
                    numbers += 1
                    numbers_sum += int(word)
                else:
                    continue
            print(f"There are {numbers} numeric strings.")
            print(f"The sum of all the numbers is {numbers_sum}.")

            print(delimiter)


            """
            Z analýzy výše se vypíše jednoduchý sloupcový graf:
            """
            print("LEN | OCCURENCES |NR")

            print(delimiter)

            num_list = []
            for word in text.split():
                word = re.sub(r'[^\w\s]', '', word)
                num_list.append(len(word))
                num_list.sort()

            occurences = {}
            for number in num_list:
                occurences[number] = num_list.count(number)

            for number, count in occurences.items():
                print(f"{number:2}| {"*" * count} |{count}")

        else:
            print("Text not found, terminating the program..")

    else:
        print("Invalid input (input has to be number), terminating the program..")

"""
Ověření uživatelského jména a hesla.
Pokud je platné uživatelské jméno i heslo, spustí se funkce analyze_text, pro kterou se jako argument zadá vybraný seznam textů:
"""
if username not in user_password:
    print("unregistered user, terminating the program..")
elif password == user_password[username]:
    analyze_text(TEXTS)
else:
    print("wrong password, terminating the program..")