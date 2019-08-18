def is_balanced(st):
    if not st:
        return True
    
    stack = []
    para = {')':'(', ']':'[', '}':'{'}
    
    for ch in st:
        if stack and ch in para and stack[-1] == para[ch]:
            stack.pop()
        else:
            stack.append(ch)
    return len(stack) == 0

# ALTERNATE CODE
def is_balanced(st):
    if not st:
        return True
    
    stack = []
    para = {'(':')', '[':']', '{':'}'}
    
    for ch in st:
        if ch in para:
            stack.append(ch)
        else:
            if not stack:
                return False
            if para[stack.pop()] != ch:
                return False
    return len(stack) == 0

assert is_balanced("")
assert is_balanced("{}")
assert is_balanced("([])")
assert is_balanced("([])[]({})")
assert not is_balanced("(")
assert not is_balanced("]")
assert not is_balanced("((()")
assert not is_balanced("([)]")
