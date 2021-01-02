import math
import time
from datetime import datetime

vars = [['git_ver','1']]
voids = [['test_void', ["print ' used test_void '", "time", "date"]]]

#for i in range(0, 10):
#    vars.append(['',''])

#vars.v.append(['var1', 9])

#print(vars.v)

def whiler(com):
    compileLine = com
    first = ''
    second = ''
    condition = ''
    voidDo = ''
    first = compileLine.split(":")[0].split()
    second = compileLine.split(":")[1].split()

    # creating condition
    for i in first:
        if i != "while":
            isVariable = False
            for j in vars:
                if j[0] == i:
                    condition += str(j[1])
                    isVariable = True
                    break
                else:
                    continue
            if isVariable == False:
                condition += str(i)
                condition += " "
        else:
                condition += " "
            
        # creating void
    voidDo = second[0]
    #print(condition)
    #print(voidDo)

    isTruth = eval(str(condition))
    if isTruth == True:
        compiler(voidDo)
        #time.sleep(0.0001)
        whiler(compileLine)


def error(num, error_type):
    print(f'\033[91mGit Error #{num} >> {error_type} \033[0m')

def compiler(t):
    if t:
        compileLine = t 
        if compileLine == "":
            print('')
        else:
            compileLines = compileLine.split()
            cl = compileLines[0]
            if cl:
                if cl == 'calc':
                    #print('Calculating')
                    calce=''
                    for i in range(0, len(compileLines)-1):
                        calce+=compileLines[i+1]
                    
                    print(eval(calce))
                elif cl == 'definedvars':
                    print('Defined vars: ')
                    for i in vars:
                        #print(i)
                        print(f'{i[0]} with value {i[1]}') 
                elif cl == 'print':
                    calce=''
                    isno = False
                    if len(compileLines)==2:
                        for io in vars:
                            if io[0] == compileLines[1]:
                                print(io[1])
                                isno = True
                                break
                    else:
                        manyBrackets = 0
                        for j in range(0,len(compileLines)):
                            if compileLines[j] == "'":
                                manyBrackets += 1
                        if manyBrackets == 2 or manyBrackets == 0:
                            if compileLines[1] == "'":
                                for i in range(0, len(compileLines)-2):
                                    if compileLines[i+2] != "'":
                                        calce += compileLines[i+2]
                                        calce += " "
                                    else:
                                        print(calce)
                        else:
                            error(1, 'Function print can\'t have more than 0 or 2 "\'" ')
                    #if isno == False:
                        #error('7', f'Variable {compileLines[1]} doesnt exist ')
                elif cl == 'gi':
                    if(compileLines[1].split('.')[1]=='gi'):
                        file = compileLines[1]
                        f = open(file, "r")
                        content = f.readlines()

                        for k in content:
                            if k == None or k == '':
                                print('')
                            else:
                                compiler(k)
                    else:
                        error('4', f'File with {compileLines[1].split(".")[1]} extension can\'t be readed')
                elif cl == 'var':
                    isPossible = True
                    for l in vars:
                        if l[0] == compileLines[1]:
                            error('2', f'Variable named {str(compileLines[1])} exist!')
                            isPossible = False
                            break
                        else:
                            continue
                    if isPossible:
                        #print(vars)
                        if len(compileLines) == 2:
                            for k in vars:
                                #print(k[0])
                                if k[0] == str(compileLines[1]):
                                    error('2', f'Variable named {str(compileLines[1])} exist!')
                                    break
                                else:
                                    vars.extend([[str(compileLines[1]), None]])
                                    #varab += 1
                                    #print(vars)   
                                    break
                        else:
                            if str(compileLines[2]) == '=':
                                calce = ''
                                manyD = 0
                                for i in range(0, len(compileLines)-3):
                                    if str(i+3) == "'":
                                        manyD += 1
                                        continue
                                    else:
                                        calce += str(compileLines[i+3])
                                        calce += " "
                                if manyD == 0 or manyD == 2:
                                    for k in vars:
                                        #print(k[0])
                                        if k[0] == compileLines[1]:
                                            error('2', f'Variable named {str(compileLines[1])} exist!')
                                            break
                                        else:
                                            try:
                                                calce = eval(calce)
                                            except:
                                                calce = calce
                                            vars.extend([[str(compileLines[1]), calce]])
                                            break
                                            #varab += 1
                                else:
                                    error('2', 'In Variable, you must use 0 or 2 "\'"') 
                            else:
                                error('5', f'In variable definition you must create it like: var NAME = value or var NAME. You use: var {compileLines[1]} {compileLines[2]}')    
                elif cl == '=':
                    strel = ''
                    isno = False
                    for i in range(0, len(compileLines)-1):
                        strel += str(compileLines[i+1])
                        strel += ' '
                    sq = strel.split()
                
                    for s in sq:
                        try:
                            s = int(s)
                        except:
                            s = s

                    #print(sq)
                    for i in range(0, len(sq)):
                        if sq[i] == "+" or sq[i] == "-" or sq[i] == "*" or sq[i] == "/" or sq[i] == "**" or sq[i] == "%" or sq[i] == "(" or sq[i] == ")" or sq[i] == "0" or sq[i] == "1" or sq[i] == "2" or sq[i] == "3" or sq[i] == "4" or sq[i] == "5" or sq[i] == "6" or sq[i] == "7" or sq[i] == "8" or sq[i] == "9":
                            sq[i]=sq[i]
                        else:
                            for j in vars:
                                if sq[i] == j[0]:
                                    sq[i] = j[1]
                                    isno = True
                    if isno == False:
                        error('7', 'Variable doesnt exist')
                    sf = ''
                    for k in sq:
                        sf += str(k)
                    print(eval(sf))


                elif cl == 'time':
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    print(f'{current_time}')
                elif cl == 'date':
                    now = datetime.now()
                    current_time = now.strftime("%d.%m.%Y")
                    print(f'{current_time}')
                elif cl == 'help' or cl == 'docs':
                    compiler('gi docs/docs.gi')
                elif cl == 'if':
                    voidDo = ''
                    condition = ''
                    firstS = ''
                    secondS = ''
                    conditionSquare = compileLine.split(":")
                    firstS = conditionSquare[0]
                    secondS = conditionSquare[1]

                    # if condition is true, void
                    secondS_splitted = secondS.split()
                    for i in secondS_splitted:
                        voidDo += i
                        voidDo += " "

                    # creating condition

                    firstS_splitted = firstS.split()
                    for i in firstS_splitted:
                        if i == "if":
                            condition += ''
                            continue
                        else:
                            isVar = False
                            # Checking is variable
                            for j in range(0, len(vars)):
                                if vars[j][0] == i:
                                    condition += str(vars[j][1])
                                    isVar = True
                                    break
                                else:
                                    continue
                            # When it isn't var
                            if isVar == False:
                                try:
                                    i = int(i)
                                    condition += i
                                except:
                                    condition += str(i)

                    isConditionTruth = eval(condition)

                    if isConditionTruth == True:
                        compiler(voidDo)
                elif cl == 'function' or cl == 'void':
                    # void name : print ' test ' , time
                    # ['test_void', ["print ' used test_void '", "time", "date"]]
                    name = compileLines[1]
                    commands = compileLine.split("=>")[1]
                    _commands = commands.split(",")
                    #print(_commands)
                    isDefined = False
                    for i in voids:
                        if i[0] == name:
                            error('8', f'Function {name} is exist!')
                            isDefined = True 
                            break     
                        else:
                            continue

                    if isDefined == False:
                        voids.extend([[name]])
                        voids[len(voids)-1].extend([_commands])
                elif cl == 'definedvoids':
                    for i in voids:
                        print(i)   
                elif cl == 'while':
                    # while condition : void
                    whiler(compileLine)
                elif cl == 'input':
                    # input TEXT
                    input_command = input(f'{compileLines[1]}')
                    for i in range(0,len(vars)):
                        if vars[i][0] == compileLines[2]:
                            vars[i][1] = input_command
                elif cl == '++':
                    for i in vars:
                        if i[0]==compileLines[1]:
                            try:
                                i[1] = int(i[1]) + 1
                            except:
                                print('')
                else:
                    isVariable = False
                    for i in vars:
                        if i[0] == cl and len(compileLines) > 1:
                            if compileLines[1] == "=":
                                cfs = ''
                                try:
                                    cfs = eval(compileLines[2])
                                except:
                                    cfs = compileLines[2]
                                i[1] = cfs
                                isVariable = True

                    if isVariable == False:
                        for i in voids:
                            if i[0] == cl:
                                for j in i[1]:
                                    compiler(j)
                    
    else:
        dbg = False



while True:
    global varab
    varab = 0
    compiler(input("> "))  
    print("")