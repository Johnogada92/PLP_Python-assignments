#creating an empty list
my_list = []

#append to my_list: 10,20,30,40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After Appending:",my_list)

#insert 15 at second position in the list
my_list.insert(1, 15)
print("After inserting 15 at position 1: ",my_list)

#extend my_list with another list: 50,60,70
my_list.extend([50, 60, 70])
print("After extending: ",my_list)

#removing the last element from my_list
my_list.pop()
print("After removing the last element: ",my_list)

#sort in ascending order
my_list.sort()
print("after sorting in ascendign order:",my_list)

#printing the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print("Index of value 30:",index_of_30)