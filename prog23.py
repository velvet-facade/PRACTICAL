#Program23
#write a python code to input names of n
#countries and their capital and currency,
#store it in a dictionary and display in tabular form
#also search and display for a particular country

#Aim
    #write a python code to input names of n
    #countries and their capital and currency,
    #store it in a dictionary and display in tabular form
    #also search and display for a particular country
# source code: -

d1 = dict()
i = 1
n = int(input("enter number of countries"))
while i <= n :
    c = input("enter country")
    cap = input("enter capital")
    curr = input("enter currency of the country")
    d1[c] = (cap , curr)
    i = i + 1
l = d1.keys()
print("\n country \t\t", "capital \t\t", "currency")
for i in l:
    z = d1[i]
    print('\n', i , '\t\t', end=" ")

for j in z:
    print(j, '\t\t', end="\t\t")
    #searching
x = input("enter country to be searched: ")
for i in l:
    if i == x:
        print("\n country \t\t","capital \t\t", "currency\t\t")
        z = d1[i]
        print("\n", i , "\t\t" , end=" ")
        for j in z:
            print(j, "\t\t", end="\t\t")
        break
#Result: program is executed successfully
