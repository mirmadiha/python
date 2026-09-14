#SET COMPREHENSION
flavoured_tea=[
    "iced ginger tea",
    "pink tea",
    "iced lemon tea",
    "coffee",
    "coffee",
    "mojito"
]
unique_tea = {tea for tea in flavoured_tea}
print(unique_tea)

recipies = {
    "Masala_chai":["milk", "sugar", "water", "sugar"],
    "Lemon_tea": ["lemon", "water", "sugar"],
    "Elaichi_chai": ["cardamom", "milk"]
}

unique_spices= {spice for ingredients in recipies.values() for spice in ingredients}
print(unique_spices)