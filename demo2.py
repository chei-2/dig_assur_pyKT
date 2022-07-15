a=[0,1,2,3,4,5,6,7,8,9]

# b=a[7:0:-1]
b=list(a.__reversed__())
print(b)
print(a)

a.reverse()

print(a)
# print(c)