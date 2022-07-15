
# a="hi how are you"
# print(id(a))
# b="hi how_are_you"
# print(id(b))
'''name = ''
while name != 'your name':   
     print('Please type your name.')     
     name = input()
print('Thank you!')'''
def divide(x, y):
    try:
         result = x / y
     except ZeroDivisionError:
         print("division by zero!")
    else:
         print("result is", result)
     finally:
        print("executing finally clause")