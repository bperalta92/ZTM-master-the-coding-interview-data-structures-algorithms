# Custom Array Implementation in Python
# Although Python provides lists as a built-in dynamic array, we can implement our own array class to understand how arrays work at a lower level.

# Objective
# We will create a custom array class with the following operations:

# Access (get)
# Push (push)
# Pop (pop)
# Insert (insert)
# Delete (delete)

# Class Definition
class MyArray():
    def __init__(self):
        self.length = 0  # Initialize the array's length to zero
        self.data = {}  # Dictionary to store array elements (keys = indices, values = data)

    # The __str__ method defines how the object is represented when printed.
    # Instead of showing a memory address, it returns a string representation of the array's attributes.
    def __str__(self):
        return str(self.__dict__)  

    def get(self, index):
        """Retrieves an element at the specified index."""
        if index >= self.length or index < 0:
            raise IndexError("Index out of bounds")  # Prevents accessing invalid indices
        return self.data[index]  
        # O(1) retrieval since dictionaries support direct key lookup.

    def push(self, item):
        """Adds an element to the end of the array."""
        self.data[self.length] = item  # Adds the item at the next available index
        self.length += 1  
        # O(1) operation, as we are simply adding an element at the end.

    def pop(self):
        """Removes and returns the last element of the array."""
        if self.length == 0:
            raise IndexError("Cannot pop from an empty array")  # Prevents errors
        last_item = self.data[self.length - 1]  # Retrieve the last element
        del self.data[self.length - 1]  # Remove last element
        self.length -= 1  # Update the length
        return last_item  
        # O(1) operation, since only the last element is removed.

    def insert(self, index, item):
        """Inserts an element at a specific index, shifting elements to the right."""
        if index > self.length or index < 0: 
            raise IndexError("Index out of bounds")  # Prevents inserting at invalid indices
        self.length += 1  
        for i in range(self.length - 1, index, -1):
            self.data[i] = self.data[i - 1]  # Shift elements right to make space
        self.data[index] = item  # Insert new element at the given index
        # O(n) operation due to shifting elements.

    def delete(self, index):
        """Deletes an element at a specific index, shifting elements to the left."""
        if index >= self.length or index < 0:
            raise IndexError("Index out of bounds")  # Prevents deleting at invalid indices
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]  # Shift elements left to fill the gap
        del self.data[self.length - 1]  # Remove the last duplicate entry
        self.length -= 1  
        # O(n) operation due to shifting elements.

# Testing the Class

arr = MyArray()

arr.push(6)  
# Adds 6 to the array
print(arr)  # {'length': 1, 'data': {0: 6}}

arr.push(2)
arr.push(9)
print(arr)  
# {'length': 3, 'data': {0: 6, 1: 2, 2: 9}}

arr.pop()  
# Removes and returns the last element (9)
print(arr)  
# {'length': 2, 'data': {0: 6, 1: 2}}

arr.push(45)
arr.push(12)
arr.push(67)
print(arr)  
# {'length': 5, 'data': {0: 6, 1: 2, 2: 45, 3: 12, 4: 67}}

arr.insert(3, 10)  
# Inserts 10 at index 3
print(arr)  
# {'length': 6, 'data': {0: 6, 1: 2, 2: 45, 3: 10, 4: 12, 5: 67}}

arr.delete(4)  
# Deletes the element at index 4
print(arr)  
# {'length': 5, 'data': {0: 6, 1: 2, 2: 45, 3: 10, 4: 67}}

print(arr.get(1))  
# Returns element at index 1 -> Output: 2

print(arr)  
# The outputs given after each function call are obtained by calling print(arr), not by the function calls themselves.

# Time Complexities
# Method	            Time    Complexity
# get(index)	        O(1)    (Direct access)
# push(item)	        O(1)    (Appending to end)
# pop()	                O(1)    (Removing last element)
# insert(index, item)	O(n)    (Shifting elements)
# delete(index)	        O(n)    (Shifting elements)

# Key Takeaways
# ✔ Why Implement a Custom Array?

# Python already provides lists, but manually implementing an array helps understand memory management and indexing.
# This implementation mimics low-level array behavior, except it uses a dictionary instead of a continuous memory block.
# ✔ Efficiency Considerations

# O(1) operations (like get(), push(), and pop()) are fast.
# O(n) operations (like insert() and delete()) require shifting elements, making them slower.
# ✔ Edge Cases Handled

# IndexError checks prevent invalid access, insertion, and deletion.
# pop() on an empty array raises an error
