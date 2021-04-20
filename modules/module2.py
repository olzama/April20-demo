def countLetters2(w, d):
    for char in w:
        if not char in d:
            # Must initialize the entry! Else, the program will explode when you try to access it in the next line!
            d[char] = 0
        d[char] += 1  # x += 1 is the same as x = x + 1
