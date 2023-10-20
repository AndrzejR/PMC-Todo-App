from extra.converters import convert
from extra.parsers import parse

while True:
    feet_inches = input("Enter feet and inches or exit: ")
    if feet_inches != "exit":
        print(convert(parse(feet_inches)))
    else:
        break
