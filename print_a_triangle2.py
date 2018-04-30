height = int(input('Give me the triangle\'s height. '))
star = '*'
line = '*'
count = 0
width = 0

while count < height:
    width += 2
    count += 1

count = 0

while count < height:
    print(line.center(width), ' ')
    count = count + 1
    line = line + star * 2
