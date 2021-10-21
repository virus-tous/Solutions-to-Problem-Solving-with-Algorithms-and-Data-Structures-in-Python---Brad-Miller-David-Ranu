import Stack

m = Stack.Stack()
m.push('x')
m.push('y')
m.push('z')

while not m.is_empty():
    m.pop()
    m.pop()
    
print(m)