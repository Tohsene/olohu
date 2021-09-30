#Question 1

import re
p= input("Input your password")
x = True
while x:  
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    # elif re.search("\s",p):
    #     break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")

#Question 2

# print("Input lengths of the triangle sides: ")
# x = int(input("x: "))
# y = int(input("y: "))
# z = int(input("z: "))

# if x == y == z:
# 	print("Equilateral triangle")
# elif x==y or y==z or z==x:
# 	print("isosceles triangle")
# else:
# 	print("Scalene triangle")

#Question 3

# models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
# print("Original list of dictionaries :")
# print(models)
# sorted_models = sorted(models, key = lambda x: x['color'])
# print("\nSorting the List of dictionaries :")
# print(sorted_models)