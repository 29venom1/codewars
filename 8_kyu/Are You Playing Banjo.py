def are_you_playing_banjo(name):
    # Create a function which answers the question "Are you playing banjo?".
    # If your name starts with the letter "R" or lower case "r", you are playing banjo!
    return name + ' ' + 'plays banjo' if name[0] == 'R' or name[0] == 'r' else name + ' ' + 'does not play banjo'
    # other solution:
    # return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo"


print(are_you_playing_banjo("rolf"))