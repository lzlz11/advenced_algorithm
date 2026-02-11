#exercise2

def is_balanced(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}


    for ch in s:
        if ch in pairs.values():
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False

   
    return len(stack) == 0
  
print(is_balanced("({[]})"))   
print(is_balanced("([)]")) 
