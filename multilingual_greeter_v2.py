from typing import Dict
from admin_options import Admin


# Populate this dictionary with at least two languages.
# Use integers for keys and strings for values.
# Example: Key = 1. Value = 'English'.
lang_dict = {
            1: "English",
            2: "Spanish",
            3: "Portuguese"
}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'What is your name?'.
name_prompt_dict = {

        1: 'What is your name?',
        2: '¿Cómo te llamas?',
        3: 'Qual é o seu nome?',
}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'Hello'.
greetings_dict = {
            1: 'Hello',
            2: 'Hola',
            3: 'Olá'

}


def print_language_options(lang_options: Dict[int, str]) -> None:
    """
    Given a dictionary, this functions iterates through the values and prints them out.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language
    :return: None
    """
    print("Please choose a language: ")
    for key in lang_options:
        #print(f'{key}: {lang_options[key]}')
        print(str(key) + ":", lang_options[key])


def language_input() -> int:
    """
    This function prompts the user for a language choice.

    :return: An integer representing the language choice made by the user
    """

    return int(input())

    # remove pass statement and implement me


def language_choice_is_valid(lang_options: Dict[int, str], lang_choice: int) -> bool:
    """
    This method determines if the choice the user made is valid.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language

    :param lang_choice: An integer representing the value the user selected
    :return: A boolean representing the validity of the lang_choice
    """
    return lang_choice in lang_options.keys()


# remove pass statement and implement me


def get_name_input(name_prompt_options: Dict[int, str], lang_choice: int) -> str:
    """
    This method takes in a dictionary and a key. It returns the value in the dictionary that has a key corresponding to
    the lang_choice parameter.

    :param name_prompt_options: A dictionary where the key is an integer representing an id and the value is a prompt
    in the users chosen language
    :param lang_choice: The language the user has chosen
    :return:
    """
    return name_prompt_options[lang_choice]


def name_input(name_prompt: str) -> str:
    """
    This function takes in a string and uses it to prompt the user for their name.

    :param name_prompt: A string in the user's chosen language that asks them for their name
    :return: The user's response when asked for their name
    """

    return input(name_prompt)  #remove pass statement and implement me


def greet(name: str, greetings_options: Dict[int, str], lang_choice: int) -> None:
    """
    Using the parameters provided, this function greets the user.

    :param name: The name the user provided
    :param greetings_options: A dictionary where the key is an integer representing a greeting and the value is a string
    with a greeting in the user's chosen language
    :param lang_choice: The language the user has chosen.
    :return:
    """
    print(f'{greetings_options[lang_choice] } {name}' + '\n')

  # remove pass statement and implement me


def run_program(ad):
    while True:
            print("press q to quit")
            choice = input("Enter \"a\" for Admin or \"u\" for User: ")
            if choice == 'a':
                option = int(input("1.) add language support \n2.) main menu \n"))
                if option == 1:
                    ad.add_language()
                    ad.add_name_prompt()
                    ad.add_greeting()
                    #print("neat")
                    #admin()
                elif option == 2:
                    continue
                else:
                    print("not a valid option")
                    raise ValueError
            elif choice == 'u':
                print_language_options(ad.lang_dict)
                chosen_lang = language_input()
                while language_choice_is_valid(ad.lang_dict, chosen_lang) is False:
                    print("Invalid selection. Try again.")
                    chosen_lang = language_input()

                selected_prompt = f"{get_name_input(ad.name_prompt_dict, chosen_lang)} \n"
                chosen_name = name_input(selected_prompt)
                greet(chosen_name, ad.greetings_dict, chosen_lang)
            elif choice == 'q':
                break

if __name__ == '__main__':
    run_program(Admin())
