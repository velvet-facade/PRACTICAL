str = input("enter a string")
n = u = lo = o = s = d = 0
for ch in str:
    if ch.isalnum():
        n+=1
        if ch.isupper():
            u+=1
        elif ch.islower():
            lo+=1
    elif ch.isdigit():
        d+=1
    elif ch.isspace():
        s+=1
    else:
        o+=1

print("no of alphabets:" , n)
print("no of capitals", u)
print("no small", lo)
print("no of digits", d)
print("no of spaces", s)
print("no of other characters", o)
