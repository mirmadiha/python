def number_list():
    return[1, 2, 3]

def numbers():
    yield 1
    yield 2
    yield 3

print(number_list())

integers = numbers()

print(integers)

print(next(integers))
print(next(integers))
print(next(integers))


