tup = (1,2,2,3,4,5,3,3,7,9,6,4,)
repeated_items = []
for i in tup:
    if(tup.count(i) > 1) and (i not in repeated_items):
        repeated_items.append(i)
print(repeated_items)
