try:
    print(eval('hello python learner'))
except SyntaxError:
    print('Invalid syntax, the expression you pass to eval() must be evaluatable')
else:
    print('code executed without exceptions')