def numbers():
    print("preparing tea....")
    order = yield
    while(True):
        print(f"\nThe order is : {order}")
        order=yield

gen = numbers()
next(gen)
gen.send("pizza")
gen.send("tea")