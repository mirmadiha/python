#SETS

drySpices = {"ginger", "chilli", "turmeric", "black pepper"}

essentialSpices = {"chilli", "cardamom", "cinamom"}

allSpices = drySpices | essentialSpices
commonSpices = drySpices & essentialSpices
print (f'union is : {allSpices}')
print (f'intersection is : {commonSpices}')
print (f'To check if ginger is part of drySpices: {"ginger" in drySpices}')
