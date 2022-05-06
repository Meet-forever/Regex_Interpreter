from pprint import pprint
class RENode:
    def __init__(self):
        self._operator = ''     # '*', '.', '+', 'leaf'
        self._symbol = ''       # only for leaf nodes
        self._position = 0      # only for non-^ leaf nodes
        self._lchild = None
        self._rchild = None     # only for . and +
        self._nullable = False
        self._firstpos = set()
        self._lastpos = set()

    def to_string(self, n):
        result = ' '*n
        if self._operator == 'leaf':
            result += 'SYMBOL: '+self._symbol
            result += ' NULLABLE='+str(self._nullable)
            result += ' FIRSTPOS='+str(self._firstpos)
            result += ' LASTPOS='+str(self._lastpos)+'\n'
        elif self._operator == '*':
            result += 'OPERATOR: STAR'
            result += ' NULLABLE='+str(self._nullable)
            result += ' FIRSTPOS='+str(self._firstpos)
            result += ' LASTPOS='+str(self._lastpos)+'\n'
            result += self._lchild.to_string(n+2)
        elif self._operator == '.':
            result += 'OPERATOR: DOT'
            result += ' NULLABLE='+str(self._nullable)
            result += ' FIRSTPOS='+str(self._firstpos)
            result += ' LASTPOS='+str(self._lastpos)+'\n'
            result += self._lchild.to_string(n+2)
            result += self._rchild.to_string(n+2)
        elif self._operator == '+':
            result += 'OPERATOR: PLUS'
            result += ' NULLABLE='+str(self._nullable)
            result += ' FIRSTPOS='+str(self._firstpos)
            result += ' LASTPOS='+str(self._lastpos)+'\n'
            result += self._lchild.to_string(n+2)
            result += self._rchild.to_string(n+2)
        else:
            result += 'SOMETHING WENT WRONG'
        return result

    def __str__(self):
        return self.to_string(0)


class ExpressionTree:
    def __init__(self, tree: RENode):
        self.tree = tree
        self.followpos = dict()
        self.dfa = []
        self.start_state = []
        self.final_states = []

    def initialize_followpos(self):
        if(self.tree != None):
            maxNum = self.tree._rchild._position
            for i in range(maxNum):
                self.followpos[i+1] = set() 

    def find_followpos(self, cur: RENode):
        if(cur == None): return
        if(cur._lchild != ''): self.find_followpos(cur._lchild)
        if(cur._operator == '.' and cur._lchild != '' and cur._rchild != ''):
            for i in cur._lchild._lastpos:
                self.followpos[i] = self.followpos[i].union(cur._rchild._firstpos)

        elif(cur._operator == '*'):
            for i in cur._lastpos:
                self.followpos[i] = self.followpos[i].union(cur._firstpos)
        
        if(cur._rchild != ''): self.find_followpos(cur._rchild)

    def generateDFA(self, letterstate):
        s0 = self.tree._firstpos
        self.start_state.append(s0)
        states = set({frozenset(s0)})
        mark = set()
        last = list(letterstate['#']).pop()
        while(len(states)>0):
            T = set(states.pop())
            mark.add(frozenset(T))
            if len(T) != 0:
                for key, val in letterstate.items():
                    U = set()
                    for p in T:
                        if p in val:
                            U = U.union(self.followpos[p])
                    if len != 0 and frozenset(U) not in mark:
                        states.add(frozenset(U))
                    if key != '#':
                        if last in T and T not in self.final_states:
                            self.final_states.append(T)
                        self.dfa.append((T, key, U))

    def matchDFA(self, inner_str)->bool:
        curstate = self.start_state[0]
        for i in inner_str:
            valid_char = False
            for j in self.dfa:
                if j[1] == i: valid_char = True
                if j[1] == i and j[0] == curstate:
                    if j[2] == set():
                        return "\tNO MATCH"
                    curstate = j[2]
                    break
            if not valid_char: return "\tNO MATCH: Invalid input character"

        if curstate in self.final_states: return "\tMATCH"
        else: return "\tNO MATCH"

    def printDFA(self):
        print(f"start_state({self.start_state[0]})")
        for i in self.dfa:
            print(f"delta{i}")
        for j in self.final_states:
            print(f"final_state({j})")

    def printFollowpos(self):
        pprint(self.followpos)


    def printTree(self, cur: RENode):
        if(cur == None):
            return
        if(cur._lchild != ''):
            self.printTree(cur._lchild)
        print(f'operator = {cur._operator}, symbol  = {cur._symbol}, position = {cur._position}, nullable = {cur._nullable}, firstpos = {cur._firstpos}, lastpos = {cur._lastpos}') # infix parsing
        if(cur._rchild != ''):
            self.printTree(cur._rchild)


class LetterState:
    def __init__(self):
        self.state = dict()
    
    def set(self, alpha, pos):
        if alpha in self.state:
            self.state[alpha] = self.state[alpha].union(set({pos}))
        else:
            self.state[alpha] = set({pos})

    def get(self):
        return self.state
    
    def clear(self):
        self.state = dict()


class Counter:
    def __init__(self):
        self.count = 1
    
    def inc(self):
        self.count += 1
    
    def get_count(self)->int:
        return self.count
    
    def clear(self):
        self.count = 1

