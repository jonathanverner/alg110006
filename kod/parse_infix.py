# coding: utf-8
def count_open_brackets(exp):
    """ Spočítá kolika otevřenými závorkami začíná seznam @exp """
    ret = 0
    for c in exp:
        if c != '(':
            return ret
        ret = ret+1
    return ret
def remove_brackets(exp):
    """ Vrátí seznam @exp bez vnějších závorek. """
    open_brackets = count_open_brackets(exp)
    counter = 0
    for c in exp[open_brackets:-open_brackets]:
        if c == '(':
            counter = counter + 1
        elif c == ')':
            if counter > 0:
                counter = counter - 1
            else:
                open_brackets = open_brackets - 1
    if open_brackets == 0:
        return exp
    return exp[open_brackets:-open_brackets]
def find_min_prec_op(exp):
    """ Najde operátor, který má nejmenší prioritu a je nejvíc vpravo
        mimo všechny závorky. """
    OPS = ['+','-','*','/']
    precedence = {'+':0,'-':0,'*':1,'/':1}
    pos = 0
    min_prec = 2
    min_pos = 0
    open_brackets = 0
    for token in exp:
        if token == '(':
            open_brackets = open_brackets + 1
        elif token == ')':
            open_brackets = open_brackets - 1
        elif token in OPS:
            if open_brackets == 0 and precedence[token] <= min_prec:
                min_pos = pos
        pos = pos + 1
    return min_pos
def parse_infix_tokenized(exp):
    """ Převede infixový výraz (zadaný jako seznam prvků) na jeho
        stromovou reprezentaci."""
    exp = remove_brackets(exp)
    if len(exp) == 1:
        return (exp[0],None,None)
    else:
        pos_op = find_min_prec_op(exp)
        L = parse_infix_tokenized(exp[:pos_op])
        R = parse_infix_tokenized(exp[pos_op+1:])
        return (exp[pos_op],L,R)
def tokenize(exp):
    """ Převede výraz zadaný jako řetězec na seznam prvků. """
    SEPS = ['+','-','*','/','(',')']
    exp = exp.replace(' ','')
    tokens = []
    token=''
    for c in exp:
        if c in SEPS:
            if len(token) > 0:
                tokens.append(token)
                token = ''
            tokens.append(c)
        else:
            token = token+c
    if len(token) > 0:
        tokens.append(token)
    return tokens
def parse_infix(exp):
    """ Převede výraz zadaný jako řetězec na jeho stromovou reprezentaci. """
    exp = tokenize(exp)
    return parse_infix_tokenized(exp)