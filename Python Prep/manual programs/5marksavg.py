# x = list(map(int, input("Enter multiple values: ").split()))
x = list(float(n) for n in input("Enter marks of 5 sub").split())
avg = sum(x)/len(x)

print(avg)
if (avg <= 100 and avg >= 80):
    print("A grade")
if (avg < 80 and avg >= 60):
    print("B grade")
if (avg < 60 and avg >= 40):
    print("C grade")
