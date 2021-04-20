
def countLetters(w):
    counts = {}
    for char in w:
        if not char in counts:
            # Must initialize the entry! Else, the program will explode when you try to access it in the next line!
            counts[char] = 0
        counts[char] += 1  # x += 1 is the same as x = x + 1
    return counts
