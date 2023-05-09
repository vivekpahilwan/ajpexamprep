dic = {'a':10, 'b':34, 'c':69, 'd':27, 'e':96}

asc = dict(sorted(dic.items(), key = lambda x : x[1]))
desc = dict(sorted(dic.items(), key = lambda x : x[1], reverse=True))

print(asc)
print(desc)
