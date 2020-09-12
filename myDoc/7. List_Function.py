numbers = [1, 2, 3, 4, 5, 6]
crush = ["Apu", "Friend"]

print(numbers)
print(crush)

# Extend add two list together
# Note: you can add the same list 
crush.extend(crush)
print(crush)

numbers.extend(crush)
print(numbers)

# Append add a specific info
# Note: add item at the end of the list
crush = ["Apu", "Friend"]

crush.append("Love")
print(crush)

# Insert to anywhere on the index
# Note: insert add new item to any index on the list and shift the previous index to the front 
# for example ex = [Foo, Bar]. ex.insert(1, 'bang'). ex = [Foor, Bang, Bar]
crush.insert(1, 'Sis')
print(crush)

# Remove the item from the list
# Note: you can remove using the variable array or the of the item
crush.remove(crush[1])
crush.remove("Friend")
print(crush)

# Clear remove everything from the list
crush.clear()
print(crush, 'cleared')

# POP remove the last item off the list
# Note: if you print the function you will get what got poped
crush = ["Apu", "Sis", "Love"]
crush.pop()
print(crush.pop())  # Print and  remove last item 
print(crush)

# Count

crush = ["Apu", "is", "Beautiful"]
crush.extend(crush)
print(crush.count("Apu"))  # Output 2\
print(crush)

# Sort
# Note: sort in ascending order
crush.sort()
print(crush)

# Reverse the order in the list
crush.reverse()
print(crush)

# Copy the list to another variable
crush = ['Apu', 'Lady M']
sis = crush.copy()
print(sis)