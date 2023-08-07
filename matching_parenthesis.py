def checkParenthesis(expression):
    stack = []
    for char in expression:
        if char in ['{', '[', '(']:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()

            match current_char:
                case '{':
                    if(char != '}'):
                        return False
                case '[':
                    if(char != ']'):
                        return False
                case '(':
                    if(char != ')'):
                        return False

    if stack:
        return False
    return True

expression = input("Enter the expression: ")
if(checkParenthesis(expression)):
    print("Balanced")
else:
    print("Not Balanced")
