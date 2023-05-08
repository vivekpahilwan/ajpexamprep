import math

#Normal 
def calculate_area(base, height):
    area = 0.5 * base * height
    return area

#Heron's formula
def calculate_area2(a, b, c):
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area


print(calculate_area(10, 5))
print(calculate_area2(5, 10, 7))
