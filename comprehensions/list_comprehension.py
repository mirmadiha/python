#LIST COMPREHENSION
menu=[
    "iced ginger tea",
    "pink tea",
    "iced lemon tea",
    "coffee",
    "mojito"
]

iced_tea=[tea for tea in menu if len(tea) < 8]
print(iced_tea)