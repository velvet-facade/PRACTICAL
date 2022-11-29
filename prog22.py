#program 22
#   write a python code to input total number of students and
#   stream name in the 11th class and display all the information
#   on the output screen using dictionary.

#Aim:
#   write a python code to input total number of students and
#   stream name in the 11th class and display all the information
#   on the output screen using dictionary.

#source code:-
classXi = dict()
n = int(input("enter number of sections in XI class: "))
i = 1
while i <= n:
    a = input("enter section")
    b = input("enter stream name")
    classXi[a] = b
    i = i + 1
print("class" , "\t" , "section", "\t", "stream Name")
for i in classXi:
    print("XI", "\t" , i , "\t", classXi[i])
#Result: The program is executed successfully
