
def to_rpn(tokens: list):
    output = []
    stack = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    associativity = {'+': 'L', '-': 'L', '*': 'L', '/': 'L'}

    for token in tokens:
        if token.isdigit() or token.replace('.', '', 1).isdigit():
            output.append(token)
        elif token in precedence:
            while (stack and stack[-1] in precedence
                   and (precedence[stack[-1]] > precedence[token] or
                        (precedence[stack[-1]] == precedence[token]
                         and associativity[token] == 'L'))):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()

    while stack:
        output.append(stack.pop())

    return output
