# Custom Array Implementation in Python
# Although arrays are pre-defined in Python in the form of lists, we can implement our own array class.
# Here, we will implement an array with some common methods such as access, push, pop, insert, and delete.

# Class Definition
# python
class MyArray():
    def __init__(self):
        self.length = 0  # Initialize the array's length to zero
        self.data = {}  # Use a dictionary to store elements (keys = indices, values = data)

    # The attributes of the array class are stored in a dictionary by default.
    # When the __dict__ method is called on an instance, it returns the attributes in a dictionary format.
    # By default, printing an instance of the class returns an object reference with its location in memory.
    # However, we can customize this behavior by overriding the __str__ method.
    
    def __str__(self):
        return str(self.__dict__)  
        # This ensures that when print(instance) is called, it returns a string representation of the array.

    def get(self, index):
        if index >= self.length or index < 0:
            raise IndexError("Index out of bounds")  # Prevent invalid access
        return self.data[index]  
        # O(1) time complexity. Directly retrieves the element at the given index.

    def push(self, item):
        self.data[self.length] = item  # Adds the item at the end
        self.length += 1  
        # O(1) time complexity. Simply appends an element.

    def pop(self):
        if self.length == 0:
            raise IndexError("Cannot pop from an empty array")  
        last_item = self.data[self.length - 1]  # Store last element
        del self.data[self.length - 1]  # Remove last element
        self.length -= 1  # Decrease the length
        return last_item  
        # O(1) time complexity. Removes and returns the last element.

    def insert(self, index, item):
        if index > self.length or index < 0: 
            raise IndexError("Index out of bounds")  # Prevent inserting at an invalid index
        self.length += 1  
        for i in range(self.length - 1, index, -1):
            self.data[i] = self.data[i - 1]  # Shift elements to the right
        self.data[index] = item  # Insert new element at the specified index
        # O(n) time complexity. Requires shifting elements.

    def delete(self, index):
        if index >= self.length or index < 0:
            raise IndexError("Index out of bounds")  # Prevent invalid deletion
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]  # Shift elements left
        del self.data[self.length - 1]  # Remove last duplicate entry
        self.length -= 1  
        # O(n) time complexity. Requires shifting elements.
Testing the Class
python
Copiar
Editar
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
# Method	Time Complexity
# get()	O(1)
# push()	O(1)
# pop()	O(1)
# insert()	O(n) (due to shifting elements)
# delete()	O(n) (due to shifting elements)
# Key Takeaways
# Python already provides lists as dynamic arrays, but implementing an array manually helps in understanding memory management.
# The dictionary-based approach allows for efficient O(1) element retrieval.
# The insert() and delete() methods require shifting elements, making them O(n) operations.
# Edge cases (e.g., out-of-bounds errors) are now handled properly in get(), insert(), and delete().
