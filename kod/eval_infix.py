OPS = ['+','-','*','/',')','(']
precedence = {'+':0,'-':0,'*':1,'/':1,'(':-1,')':-1}
def reduce_stack(op_stack, arg_stack, prec):
    while len(op_stack) > 0 and precedence[op_stack[-1]] >= prec:
        op = op_stack.pop()
        if op == '(':
            return
        a1,a2 = arg_stack.pop(), arg_stack.pop()
        if op == '+':
            arg_stack.append(a1+a2)
        elif op == '-':
            arg_stack.append(a1-a2)
        elif op == '*':
            arg_stack.append(a1*a2)
        elif op == '/':
            arg_stack.append(a1/a2)

def eval_infix(token_list):
    op_stack = []
    arg_stack = []
    number_stack = []
    for token in token_list:
        if token in OPS:
            if token == '(':
                op_stack.append(token)
            else:
                reduce_stack(op_stack,arg_stack,precedence[token])
                if token != ')':
                    op_stack.append(token)
        else:
            arg_stack.append(token)
    reduce_stack(op_stack,arg_stack,-1)
    return arg_stack.pop()
