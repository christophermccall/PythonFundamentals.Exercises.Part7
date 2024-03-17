from typing import Dict

# Populate this dictionary with at least two languages.
# Use integers for keys and strings for values.
# Example: Key = 1. Value = 'English'.


class Admin:

    def __init__(self):
        self.lang_dict = {
            1: ["English"],
            2: ["Spanish"],
            3: ["Portuguese"],
        }

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'What is your name?'.
        self.name_prompt_dict = {
            1: ['What is your name?'],
            2: ['¿Cómo te llamas?'],
            3: ['Qual é o seu nome?'],
        }

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'Hello'.
        self.greetings_dict = {
            1: ['Hello'],
            2: ['Hola'],
            3: ['Olá'],
        }

    def add_language(self):
        key = len(self.lang_dict)+1
        value = input("enter a new language: ")
        storage_dict = {key: [value]}
        self.lang_dict.update(storage_dict)
        self.greetings_dict.update({key:[]})
        print(self.lang_dict)

    def add_greeting(self):

        print(self.lang_dict)
        choice = input("select a language via number: ")
        if int(choice) in self.greetings_dict.keys():
            self.greetings_dict[int(choice)] += input().split() #.values({int(choice): input("enter a new greeting: "),})
            print(self.greetings_dict)



