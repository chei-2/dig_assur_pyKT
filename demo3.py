'''
from collections import deque
queue = deque(["Eric", "John", "Michael"])
print(queue)
queue.append("Terry")           # Terry arrives
queue.append("Graham")     
print(queue)     # Graham arrives
queue.popleft()                 # The first to arrive now leaves
print(queue)
queue.popleft() 
print(queue)                # The second to arrive now leaves
queue.pop()
print(queue)
            

x = 15

x ^= 3

print(x) ''' 



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[]
#newlist.extend(fruits)
newlist = fruits.copy()
print(newlist)
#newlist = [x if x != "banana" else "orange" for x in fruits]
for i in range(len(newlist)):
    if newlist[i] == "banana":
        newlist.insert(i,"orange")
        newlist.remove('banana')

print(newlist)
#     else:
#         break
#         newlist.append(i)


# if "banana" in newlist():
#     newlist.remove('banana')
#     newlist.append("orange")


print(newlist)
'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[]
for i in range(len(fruits)):
    if fruits[i] == "banana":
        fruits[i] = 'orange'
    else:
        pass
print(fruits)'''
