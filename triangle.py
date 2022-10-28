"""A Python classify triangle"""


def classify(a, b, c):
    print('classify triangle(a,b,c)')
    a = int(input('enter a value: '))
    b = int(input('enter b value: '))
    c = int(input('enter c value: '))

    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    if a == b == c:
        return 'Equilateral'

    elif (round((a ** 2), 0) + round((b ** 2), 0)) == round((c ** 2), 0):
        return 'Right'

    elif a != b and b != c and c != a:
        return 'Scalene'

    else:
        return 'Isoceles'

