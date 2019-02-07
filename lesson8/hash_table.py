def my_index(value):
    letter = 26
    index = 0
    size = 20000

    for i, char in enumerate(value):
        index += (ord(char) - ord('a') + 1) * letter ** i

    return index % size

a = 'apple'
b = 'hard'
c = 'pig'
d = 'donation'

print(my_index(a))
print(my_index(b))
print(my_index(c))
print(my_index(d))