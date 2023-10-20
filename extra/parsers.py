def parse(feet_inches):
    feet = int(feet_inches.split(" ")[0])
    inches = int(feet_inches.split(" ")[1])
    return feet, inches
