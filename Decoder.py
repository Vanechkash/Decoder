from sys import argv

file = open(argv[1], 'r')
letter = list(file.read())
print('letter received...')

outletter = []

for i in range(len(letter)):
    try:
        if letter[0] == letter[1]:
            del letter[1]
            del letter[0]
        else:
            outletter.append(letter[0])
            del letter[0]
    except:
        # когда последняя буква письма непарная
        if len(letter) == 1:
            outletter.append(letter[0])
            del letter[0]

outletter = ''.join(outletter)
print('decoded letter: ' + outletter)