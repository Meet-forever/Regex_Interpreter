from REParser import parser
from RENode import ExpressionTree
from REParser import lts
from REParser import counter
import sys


def read_input1():
    result = ''
    while True:
        data = input('REGEX: ').strip()
        if ';' in data:
            i = data.index(';')
            result += data[0 : i+1]
            break
        else:
            result += data + ' '
    return result

def read_input2():
    result = ''
    while True:
        data = input('\tINPUT STRING: ')
        if ';' in data:
            i = data.index(';')
            result += data[0 : i]
            break
        else:
            result += data + ''
    return result


def main():
    dfa_flag = False
    if (len(sys.argv) > 1):
        if(sys.argv[1] == '-dfa'):
            dfa_flag = True
    while True:
        data = read_input1()
        if data == 'exit;':
            print("Have a Great Day!  :)\n")
            break
        try:
            tree = parser.parse(data)
            if tree != None:
                et = ExpressionTree(tree)
                # et.printTree(et.tree)
                et.initialize_followpos()
                et.find_followpos(et.tree)
                # et.printFollowpos()
                et.generateDFA(lts.get())
                if dfa_flag:
                    et.printDFA()
                while True:
                    innerData = read_input2()
                    if innerData == 'exit':
                        break
                    try:
                        ans = et.matchDFA(innerData)
                        print(ans)

                    except Exception as inst2:
                        print(inst2.args[0])
                        continue
                lts.clear()
                counter.clear()
                # print(lts.get()) # prints letterstate
        except Exception as inst:
            lts.clear()
            counter.clear()
            print(inst.args[0]) 
            # print(tree if tree else '') # Debug
            continue

main()

