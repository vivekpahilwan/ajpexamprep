list = [1,2,3,4,5,6,7,8,9,0]

# accessing values in list 2 ways
# by providing index value
print(list[2])

# by using slicing
print(list[2:7])
print(list[2:7:2]) # skips 1 element in between
print(list[2:7:2])


# deleting values in list 3 ways
# pop, del, clear

#pop by providing index number
print(list.pop(2))

#del
del list[len(list)-1] # deletes the last item by providing the index of last item using len funcion
print(list)

#remove func
list.remove(4)
print(list)

#Clear function
list.clear()
print(list)

# updating 
l2 = [5,6,7,8]
for i in l2:
    list.append(i)

print(list)