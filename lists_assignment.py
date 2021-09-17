#Question 1

my_list = ['this', True, 'student', 45, 66, 43]
new_list = my_list.copy()
print(new_list)


#Question 2

color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color_list.remove('Red')
color_list.remove('Pink')
color_list.remove('Yellow')
print(color_list)


#Question 3

color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = input("What is your favourite color")
color_list.append(color)
print(color_list)

#Question 4

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)