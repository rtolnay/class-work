def chop(c):
    del c[len(c)-1]
    del c[0]

letters = ['r', 'y', 'a', 'n']
chop(letters)
print(letters)
