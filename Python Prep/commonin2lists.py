l1 = list(int(i) for i in input("Enter 1st List").split())
l2 = list(int(i) for i in input("Enter 2nd List").split())

# for a in l1:
#     for b in l1:
#         if a == b:
#             print(a)

common_list = [c for c in l1 if c in l2]
print(common_list)
