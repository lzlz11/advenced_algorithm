#exercise2

def is_balanced(expression):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}


    for char in expression:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False

   
    return len(stack) == 0
  
print(is_balanced("({[]})"))   
print(is_balanced("([)]")) 
