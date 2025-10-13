def isValid(s: str) -> bool:
    stack = []
    open_brackets = "({["
    close_brackets = ")}]"

    for char in s:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if not stack:
                return False
            top = stack.pop()
            if open_brackets.index(top) != close_brackets.index(char):
                return False
    return len(stack) == 0


print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
