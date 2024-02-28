def reversed_string(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string


print(reversed_string("Zak"))
print(reversed_string("Leeeeeeeel"))
