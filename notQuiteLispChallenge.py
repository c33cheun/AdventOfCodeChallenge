from sys import stdin

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    

file_obj = open("input.txt","r")

# Main program execution
brackets = str(file_obj.read())
s = Stack()

for char in brackets:
    if (not s.isEmpty() and s.peek() == "(" and char == ")"):
        s.pop()
    else:
        s.push(char)

count = 0
for i in range(s.size()):
    char = s.pop();
    if (char == "("):
        count = count + 1
    else:
        count = count - 1

