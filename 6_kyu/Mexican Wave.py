def wave(people):
    print([people[:c]+people[c].upper()+people[c+1:] for c in range(len(people))if people[c] != ' '])


wave('two words')


