#Aim: to write a python program to accept value from the user and create a tuple
# Source code:-
t = tuple()
n = int(input("enter any number"))
for i in range(n):
    a = int(input("enter number"))
    t = t+(a,)
print("output is")
print(t)
