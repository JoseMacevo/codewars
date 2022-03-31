"""
The Western Suburbs Croquet Club has two categories of membership, Senior
and Open. They would like your help with an application form that will tell
prospective members which category they will be placed.

To be a senior, a member must be at least 55 years old and have a handicap
greater than 7. In this croquet club, handicaps range from -2 to +26; the
better the player the lower the handicap.

Input

Input will consist of a list of pairs. Each pair contains information for a
single potential member. Information consists of an integer for the person's
age and an integer for the person's handicap.

Output

Output will consist of a list of string values (in Haskell: Open or Senior)
starting whether the respective member is to be placed in the senior or open
category.

Example

input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]


"""


def open_or_senior(data):
    new_lst = [element for element in data]
    output_lst = []
    for i in new_lst:
        age, handicap = i
        if age < 55 or handicap <= 7:
            output_lst.append("Open")
        else:
            output_lst.append("Senior")

    return output_lst   


print(open_or_senior([(29, 22), (33, 14), (54, 0), (19, 9), (82, 7), (87, 1)]))
