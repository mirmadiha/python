def numbers():
    count = 1
    while(True):
        yield count
        count += 1

gen = numbers()
for num in range(1,5):
    print(next(gen)) 
