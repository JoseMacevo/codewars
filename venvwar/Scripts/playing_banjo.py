"""
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing
banjo!

The function takes a name as its only argument, and returns one of the
following strings:

name + " plays banjo"
name + " does not play banjo"

Names given are always valid strings.
"""


def are_you_playing_banjo(name):
    new_lst = []
    for letter in name:
        new_lst.append(letter)

    if new_lst[0] == "R":
        return f"{name} plays banjo"

    elif new_lst[0] == 'r':
        return f"{name} plays banjo"

    else:
        return f"{name} does not playing banjo"
