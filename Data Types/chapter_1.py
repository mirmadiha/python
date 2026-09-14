#mutability of an object is checked by identity not by value

age = 20 
print(f"Jack's age is {age}")
print(f"id: {id(age)}")

age = 25
print(f"Jack's age after 5 years is {age}")
print(f"id: {id(age)}")

# since we got different id's numbers are immutable !

