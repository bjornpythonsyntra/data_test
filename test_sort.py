a = [1,2,3,4]
b = a
c = b
a.append(7)
b.append(11)
c.append(6)
a.sort()
print(a,b,c)