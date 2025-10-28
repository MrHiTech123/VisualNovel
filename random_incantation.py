from random import randint, choice

linear_a_chars = ''.join([chr(x) for x in range(0x10600, 0x10736 + 1)])


length = randint(5, 10)

print(''.join([choice(linear_a_chars) for x in range(length)]))
