users = [
    {"id":1, "total":200, "coupon":"P10"},
    {"id":2, "total":150, "coupon":"P20"},
    {"id":3, "total":450, "coupon":"P30"}
]

discounts={
    "P10":(0.2,0),
    "P20":(0.5,0),
    "P30":(0,10)
}

for user in users:
    percent, fixed = discounts.get(user["coupon"],(0,0))
    discount=user["total"] * percent + fixed
    print(f'user with id {user["id"]} paid {user["total"]} and got discount of Rs. {discount}')
