from random import choice
import sys

def generate_model(text, order):
    model = {}
    for i in range(0, len(text) - order):
        fragment = text[i:i + order]
        next_letter = text[i + order]
        if fragment not in model: 
            model[fragment] = {}
        if next_letter not in model[fragment]: 
            model[fragment][next_letter] = 1
        else:
            model[fragment][next_letter] += 1
    return model


def get_next_character(model, fragment):
    letters = []
    for letter in model[fragment].keys():
        for times in range(0, model[fragment][letter]):
            letters.append(letter)
    return choice(letters)


def generate_text(text, order, length):
    model = generate_model(text, order)
    current_fragment = text[0:order]
    output = ""
    for i in range(0, length - order):
        new_character = get_next_character(model, current_fragment)
        output += new_character
        current_fragment = current_fragment[1:] + new_character
    print(output)


text = "some sample text"
if __name__ == "__main__":
    generate_text(text, int(sys.argv[1]), int(sys.argv[2]))