import ply.yacc as yacc
from RENode import RENode
from RELexer import tokens
from pprint import pprint
from RENode import Counter
from RENode import LetterState

counter = Counter()
lts = LetterState()

def p_start(p):
    '''start : re SEMI'''
    parent = RENode()
    right = RENode()
    right._symbol = '#'
    right._operator = 'leaf'
    right._position = counter.get_count()
    right._firstpos.add(right._position)
    right._lastpos.add(right._position)
    lts.set('#', right._position)
    counter.clear()  
    parent._operator = '.'
    parent._lchild = p[1]
    parent._rchild = right  
    parent._nullable =  parent._lchild._nullable and parent._rchild._nullable
    if(parent._lchild._nullable):
        parent._firstpos = parent._lchild._firstpos.union(parent._rchild._firstpos)
    else:
        parent._firstpos = parent._lchild._firstpos

    if(parent._rchild._nullable):
        parent._lastpos = parent._lchild._lastpos.union(parent._rchild._lastpos)
    else:
        parent._lastpos = parent._rchild._lastpos
    p[0] = parent
    # p[0] = ['.', p[1], '#']



def p_re(p):
    '''re : re PLUS term'''
    plus = RENode()
    plus._operator = '+'
    plus._lchild = p[1]
    plus._rchild = p[3]
    plus._nullable = plus._lchild._nullable or plus._rchild._nullable
    plus._firstpos = plus._lchild._firstpos.union(plus._rchild._firstpos)
    plus._lastpos = plus._lchild._lastpos.union(plus._rchild._lastpos)
    p[0] = plus
    # p[0] = ['+', p[1], p[3]]


def p_re_base(p):
    '''re : term'''
    p[0] = p[1]


def p_term(p):
    '''term : term factor'''
    dot = RENode()
    dot._operator = '.'
    dot._lchild = p[1]
    dot._rchild = p[2]
    dot._nullable =  dot._lchild._nullable and dot._rchild._nullable
    if(dot._lchild._nullable):
        dot._firstpos = dot._lchild._firstpos.union(dot._rchild._firstpos)
    else:
        dot._firstpos = dot._lchild._firstpos

    if(dot._rchild._nullable):
        dot._lastpos = dot._lchild._lastpos.union(dot._rchild._lastpos)
    else:
        dot._lastpos = dot._rchild._lastpos

    p[0] = dot
    # p[0] = ['.', p[1], p[2]]


def p_term_base(p):
    '''term : factor'''
    p[0] = p[1]


def p_factor(p):
    '''factor : factor STAR'''
    star = RENode()
    star._operator = '*'
    star._nullable = True
    star._lchild = p[1]
    star._firstpos = star._firstpos.union(star._lchild._firstpos)
    star._lastpos = star._lastpos.union(star._lchild._lastpos)
    p[0] =  star
    # p[0] = ['*', p[1]]


def p_factor_base(p):
    '''factor : basement'''
    p[0] = p[1]


def p_basement_letter(p):
    '''basement : LETTER'''
    letter = RENode()
    letter._symbol = p[1]
    letter._operator = 'leaf'
    letter._position = counter.get_count()
    counter.inc()
    letter._firstpos.add(letter._position)
    letter._lastpos.add(letter._position)
    lts.set(p[1], letter._position)
    p[0] = letter
    # p[0] = p[1]


def p_basement_epsilon(p):
    '''basement : EPSILON'''
    end = RENode()
    end._operator = 'leaf'
    end._symbol = '^' 
    end._nullable = True
    p[0] = end
    # p[0] = p[1]


def p_basement_re_run(p):
    '''basement : LPAREN re RPAREN'''
    p[0] = p[2]


def p_error(p):
    counter.clear()
    lts.clear()
    print("Error in the parser")


parser = yacc.yacc()