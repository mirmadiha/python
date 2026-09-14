#DICTIONARY COMPREHENSION
tea_price_inr={
    "Masala_Chai":20,
    "Lemon_Tea": 15,
    "Ginger_Tea": 25
}

tea_price_usd = {tea: price/80 for tea, price in tea_price_inr.items()}
print(tea_price_usd)