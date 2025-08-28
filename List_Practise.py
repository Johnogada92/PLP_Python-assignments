list_a = [1,2,3,4,5]
#index    0 1 2 3 4
print("Before AAppend:", list_a)
print(list_a[3])
print(list_a)
list_a[0] = 10
print(list_a)
print(len(list_a))
list_a.insert(len(list_a), 6) #using insert to add a number to list
print(list_a)
list_a.append(7) #using append to add a number to list
print("After Append:", list_a)
list_a.extend([8, 9, 10, 15]) #Using extend to add a number to list
print(list_a)

#Deleting a number or value e can use:
list_a.pop(8)
print(list_a)
del list_a[7]
print(list_a)


list_b = [1, "today", True, 3.0]
print(list_b)
list_c = ["skinny","amazing","cool"]
list_d = [1,2,3,[4,5],6,7]
prime_numbers = [1,3,5]
print("List1:",prime_numbers)
even_numbers = [4,6,8]
print("List2:",even_numbers)

#to join the two lists we can use append ie
prime_numbers.extend(even_numbers)
print("Lists after append:",prime_numbers)
prime_numbers.remove(6)
print("Lists after deleting/removing 6:",prime_numbers)

numbers = [number*number for number in range(1,100)]
print(numbers)
numbers = [numbers*x for x in range(1,0)]
print(numbers)

#python tuples #craeting a tuuple

