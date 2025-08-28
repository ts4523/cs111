"""r = 0 #radius
h = 0 #height
l = 0 #length
A = 0 #Area
#n = []

shape = input("What is the shape?: \n")
if shape == "circle":
    r = input("What is the radius?: \n")
    A = 3.14(r*r)
    print(f"Area = {A}")
elif shape == "square":
    h = input("What is the height?: \n")
    l = input("What is the length?: \n")
    A = h*l
    print(f"Area = {A}")
elif shape == "rectangle":
    h = input("What is the height?: \n")
    l = input("What is the length?: \n")
    A = h*l
    print(f"Area = {A}")
else:
    print("Check spelling. Answers must be all lower case. \n")"""

def MyCoolFunction(x,y):
    return 2*x + y - 1
A = 5
B = 0
C = MyCoolFunction(A,B)
print(C)