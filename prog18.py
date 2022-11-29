# Aim: -
#   To write a python program to shift the negative
#   numbers to left and positive numbers to the right

#original list: [-12, 11,-13,-5,6,-7,-3,-6]
# Expected output:- [11,6,5,-6,-3,-5,-13,-12]

#Source code:-
l = [-12, 11,-13,-5,6,-7,-3,-6]
n = len(l)
print("original list: ", l)
for i in range(n-1):
    for j in range(n-i-1):
        if l[j] < 0:
            l[j], l[j+1] = l[j+1], l[j]
print("after shifting list: ", l)
