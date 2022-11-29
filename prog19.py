#Aim: write a pythonprogram for an element in a given list
#Source code:-
l = eval(input("enter the elements"))
n = len(l)
item = eval(input("enter element to be searched"))
for i in range(n):
    if l[i] == item:
        print("element found at position", i+1)
        print("element index: ", l.index(item))
        break
else:
    print("element not found")
