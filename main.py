from tokenize import tokenize
from shunting import to_rpn

expr = input("type a expression: ")
tokens = tokenize(expr)
rpn = to_rpn(tokens)

print("expression in RPN:", rpn)