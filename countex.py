arr = ["aoo", "boo", 'coo', 'aoo', ['aoo','aoo'],'aoo','aoo','aoo',]
'''print(arr.count('aoo'))
if arr.count("aoo") > 1:
    for i in range(arr.count("aoo")-1):

        arr.remove('aoo')
    print(arr)

newarr=[]
newarr = list(dict.fromkeys(arr))
print(newarr)'''

s = set(arr)
print(s)