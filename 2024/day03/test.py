from collections import deque
import re

# Create an empty stack using deque
stack = deque()

# Push elements onto the stack (LIFO order)
stack.append(10)  # Push 10 onto the stack
stack.append(20)  # Push 20 onto the stack
stack.append(30)  # Push 30 onto the stack

print("Stack after pushes:", stack)

# Pop an element from the stack (LIFO order)
top_element = stack.pop()  # Pop the last element added
print("Popped element:", top_element)
print("Stack after pop:", stack)

# Push more elements
stack.append(40)
stack.append(50)
print("Stack after more pushes:", stack)

# Pop another element
top_element = stack.pop()
print("Popped element:", top_element)
print("Stack after pop:", stack)

# Check if stack is empty
if not stack:
    print("Stack is empty.")
else:
    print("Stack is not empty.")

pattern = r"(-?\d+)"
matches = re.findall(pattern, "mul(3,3)")
print(matches[0])

input="toto"

print(input[1:3])
