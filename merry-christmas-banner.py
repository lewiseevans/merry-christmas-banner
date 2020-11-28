#import unicornhat as unicorn

print("Simple program to display Merry Christmas on a 16x16 colourful display")

# unicorn.set_layout(unicorn.PHAT)

# R G R G R G
# G R G R G R


def banner(row, col):

    r = "R"
    g = "G"
    if row % 2 == 0:
        if col % 2 == 0:
            return r
        else:
            return g
    else:
        if col % 2 == 0:
            return g
        else:
            return r


actualBanner = ""
row = 0
while row < 2:
    col = 0
    actualBanner += "\n"
    while col < 16:
        actualBanner += banner(row, col)
        col += 1
    row += 1

print(actualBanner)
