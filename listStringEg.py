# Remove fruits from basket2 that are present in basket1
basket1 = ["kiwifruits","grapefruits","apples","apricots","nectarines","oranges","pears"]
basket2 = ["lemons","apples","grapes","apricots","dragonfruits","peaches","pears"]
for item in basket1:
    if item in basket2:
        basket2.remove(item)
        

print('Basket 1: ' + str(basket1))
print('Basket 2: ' + str(basket2))
