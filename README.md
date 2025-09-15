List Operations Assignment
This repository contains a Python script that demonstrates fundamental list operations as outlined in a programming assignment.

Assignment Objectives
The script performs the following sequence of operations on a Python list:

Creates an empty list.

Appends elements to the list.

Inserts an element at a specific position.

Extends the list with another list.

Removes the last element.

Sorts the list in ascending order.

Finds and prints the index of a specific value.

Code Overview
The main script is located in list_operations.py. It clearly executes each step of the assignment and prints the state of the list after each operation for clarity.

Operations Demonstrated:
Create List: my_list = []

Append: my_list.append(10), etc.

Insert: my_list.insert(1, 15)

Extend: my_list.extend([50, 60, 70])

Remove last element: my_list.pop()

Sort: my_list.sort()

Find Index: my_list.index(30)

How to Run
Prerequisites: Ensure you have Python 3.x installed on your system.

Clone the repository:

bash
git clone https://github.com/python-assignment/list-operations-assignment.git
cd list-operations-assignment
Run the Python script:

bash
python list_operations.py
Expected Output
When you run the script, you should see the following output in your terminal, showing the list's state after each operation:

text
After appending 10, 20, 30, 40: [10, 20, 30, 40]
After inserting 15 at position 1: [10, 15, 20, 30, 40]
After extending with [50, 60, 70]: [10, 15, 20, 30, 40, 50, 60, 70]
After removing last element: [10, 15, 20, 30, 40, 50, 60]
After sorting in ascending order: [10, 15, 20, 30, 40, 50, 60]
Index of value 30: 3
