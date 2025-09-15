#list of intergers
numbers = [10,20,30,40,50]

#computation
total = sum(numbers)

#result
print("The total for all numbers is ", total)

#challenge no.2
#create tuple
favorite_books = {
    "The river and the source"
    "Narrow Road",
    "Big city Boys",
    "Boys to Men",
    "The seven Church ages"
}
#print using a loop
for book in favorite_books:
    print(book)

#challenge no. 3
#create an empty dictionary
person_info = {}

#user input
person_info['name'] = input("Enter Your Name: ")
person_info['age'] = input("Enter Your age: ")
person_info['favorite_food'] = input("Enter Your favorite_Food: ")

#print the dictionary
print("Here is the information you entered: ")
print(person_info)
print("Please check that the information provided is the corrct one...")

#challenge 4
#get input/ convert to sets
set1 = set(map(int,input("Enter numbers for set1 separated by space: ")))
set2 = set(map(int,input("Enter numbers for set2 separated by space: ")))

#intercession (commn elements)
common_Elements = set1 & set2

print("common_elements are: ",common_Elements)

#challenge 5
#storing list of words

words = ["Footbal","Volleyball","Handball","Netball","Soccer"]

#using list comprehension to filter

add_Length_words = [word for word in words if len(word) % 2 != 0]

#result
print("Words with an odd number of characters: ",add_Length_words)
