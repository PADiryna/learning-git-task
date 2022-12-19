print("Shopping list")
dct = {"bakery": ["bread", "buns","donuts"],
"vegetable shop" :["carrot", "celery", "arugula"]}
for k, v in dct.items():
   print("I am going to the", k.capitalize(), "and buy such products", v)
all = (len(dct["bakery"])+len(dct["vegetable shop"]))
print("Buy",all,"products together")


