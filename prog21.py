# Program21:Write a python program to input any two tuples and swap their values
#Aim: to Write a python program to input any two tuples and swap their values
#source code:
t1 = ()
n = int(input("Total number of values in the first tuple"))
for i in range(n):
    a = input("enter elements")
    t1 = t1 + (a,)
t2 = tuple()
m = int(input("enter the number of values in second tuple."))
for i in range(m):
    a = input("enter elements")
    t2 = t2 + (a,)
print("first tuple:")
print(t1)
print("second tuple:")
print(t2)
t1, t2 = t2, t1
print("after swapping:")
print("first tuple:")
print(t1)
print("second tuple:")
print(t2)

#Result: program is successfully executed.
