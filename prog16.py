# Aim: To display frequencies of all elements of a list
#Source code:
n = int(input("enter the number of elements"))
a = []
l1 = []
l2 = []
for i in range(n):
    s = int(input("enter number"))
    a.append(s)
print("list items", a)
for i in a:
    if i not in l2:
        x = a.count(i)
        l1.append(x)
        l2.append(i)
print("Elements", "\t\t\t", "frequency")
for i in range(len(l1)):
    print(l2[i], "\t\t\t", l1[i] )
