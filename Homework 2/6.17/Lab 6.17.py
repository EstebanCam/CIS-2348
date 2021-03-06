'''
Esteban Camarillo
ID #:1636095
lab:6.17


'''



words = input()

password = ''


for char in words:

    if (char == 'i'):
        words = words.replace('i','!')


    if (char == 'a'):
        words = words.replace('a','@')

    if (char == 'm'):
        words = words.replace('m','M')

    if (char == 'B'):
        words = words.replace('B','8')

    elif (char == 'o'):
        words = words.replace('o','.')

password = (words + 'q*s')


print(password)



