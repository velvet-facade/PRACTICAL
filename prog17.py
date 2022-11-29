#Aim: to write a python code to display those
#strings which are string with 'A' of given list

#Souce code:-
l = ["Anshim","Leena","Akthar","Tuba","Nishant","Amal"]
count = 0
for i in l:
    if i[0] in "aA":
        count = count+1
        print(i)
print("Appearing", count, "times")

# program executed succesfully.
