height = int(input('Give me the triangle\'s height. '))
star = '*'
new_star = '**'
count = 0
width = 0

while count < height:
    width += 2
    count += 1

count = 0

while count < height:
    print(star.center(width), ' ')
    count = count + 1
    star = star + new_star
