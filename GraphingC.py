import matplotlib.pyplot as plt
import GraphMathModule as mathfunction
print("Type 'options' for more, or type 'options' + specified option to get the specified option's description.")

storagevar = []
storageval = []
invalidvar = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '/', '+', '-', '*', '\\', '<', '>', '=', '%']

credits = "Credits to Avi Seth (Github username: TheScienceComputerNerd) for creation."

options1 = ["options", "prev", "calc", "graph", "exit", "credits"]
desc1 = ["Format: options OPTION\nDescription: Used to give options of a prompt available. Type 'options' for all options, or attach the specific option's name to get it's description.",
         "Format: prev VAR\nDescription: Type 'prev' to get all stored variables. Attach a stored variable's name to get it's value.",
         "Format: calc\nDescription: Takes you to the command line prompt for mathematical calculations.",
         "Format: graph\nDescription: Takes you to the command line prompt for graphing functions (without vertical asymptotes).",
         "Format: exit\nDescription: Closes program.",
         "Format: credits\nDescription: Lists credits."]

optionscalc = ["options", "prev", "storemode", "delete", "synDiv", "fac", "tylrcos", "tylrsin", "arccos", "polyDeriv", "lim", "RieSum", "ln", "e", "pi", "exit"]
descalc = ["Format: options OPTION\nDescription: Used to give options of a prompt available. Type 'options' for all options, or attach the specific option's name to get it's description.",
         "Format: prev VAR\nDescription: Type 'prev' to get all stored variables. Attach a stored variable's name to get it's value.",
         "Format: storemode BOOL\nDescription: BOOL is a boolean value. If BOOL == True, asks for a prompt 'Var: ' to store each calculation as a one-letter variable. If BOOL == False, it returns calculations in the command line.",
         "Format: delete VAR\nDescription: Deletes the associated variable from storage.",
         "Format: synDiv B POLY RES\nDescription: Performs synthetic division using POLY as a polynomial in list form without spaces (the position of coefficients in the list represents degree, where the first term in the list is the leading coefficient) and B as the input. If RES = 0, gives quotient polynomial only. If RES = 1, gives remainder only.",
         "Format: fac NUM\nDescription: Returns the factorial of the number NUM.",
         "Format: tylrcos TERMS\nDescription: Returns the taylor series polynomial for cosine give TERMS taylor terms",
         "Format: tylrsin TERMS\nDescription: Returns the taylor series polynomial for sine give TERMS taylor terms",
         "Format: polyDeriv POLY\nDescription: Returns the derivative polynomial of POLY, given POLY is in list form (wihout spaces)"
         "Format: lim VAL POLY1 POLY2 DIRECTION\nDescription: Limit, as x approaches VAL ('-inf', number values, or 'inf'), of POLY1/POLY2 (where POLY1 and POLY2 are both polynomials in list form), from DIRECTION direction (DIRECTION = 'left' or 'right')",
         "Format: rieSum LB UB POLY DX\nDescription: The Riemann Sum of polynomial POLY with LB as lower bound and UB as upper bound, and DX is dx",
         "Format: exit\nDescription: Takes you to the parent prompt."]

breaker = True
while breaker:
    prompt = input("<<< ")
    prompt = prompt.split()
    if len(prompt) == 0:
        None
    elif prompt[0] == 'options':
        if len(prompt) == 1:
            for item in options1:
                print(item)
        elif len(prompt) == 2:
            if prompt[1] in options1:
                print(desc1[options1.index(prompt[1])])
            else:
                print("OptionError: Option does not exist")
        else:
            print("OptionError: Option does not exist")
    elif prompt[0] == 'prev':
        if len(prompt) == 1:
            for item in storagevar:
                print(item)
        elif len(prompt) == 2:
            if prompt[1] in storagevar:
                print(storageval[storagevar.index(prompt[1])])
            else:
                print("VarError: Undefined variable")
        else:
            print("VarError: Undefined variable")
    elif prompt[0] == 'calc':
        calcbreaker = True
        storemode = False
        while calcbreaker:
            prompt = input("calc/<<< ")
            prompt = prompt.split()
            if len(prompt) == 0:
                None
            elif prompt[0] in storagevar:
                print(eval(storageval[storagevar.index(prompt[0])]))
            elif prompt[0] == 'options':
                if len(prompt) == 1:
                    for item in optionscalc:
                        print(item)
                elif len(prompt) == 2:
                    if prompt[1] in optionscalc:
                        print(descalc[options1.index(prompt[1])])
                    else:
                        print("OptionError: Option does not exist")
                else:
                    print("OptionError: Option does not exist")
            elif prompt[0] == 'prev':
                if len(prompt) == 1:
                    for item in storagevar:
                        print(item)
                elif len(prompt) == 2:
                    if prompt[1] in storagevar:
                        print(storageval[storagevar.index(prompt[1])])
                    else:
                        print("VarError: Undefined variable")
                else:
                    print("VarError: Undefined variable")
            elif prompt[0] == 'storemode':
                if len(prompt) == 2:
                    if prompt[1] == 'True' or prompt[1] == 'False':
                        storemode = eval(prompt[1])
                    else:
                        print("FunctionError: Function only accepts boolean values for parameter BOOL")
                else:
                    print("FunctionError: Function uses 1 parameter")
            elif prompt[0] == 'delete':
                if len(prompt) == 2:
                    if prompt[1] in storagevar:
                        r = eval(prompt[1])
                        del(storageval[storagevar.index(prompt[1])], storagevar[storagevar.index(prompt[1])], r)
                    else:
                        print("VarError: Undefined Variable")
                else:
                    print("FunctionError: Function uses 1 parameter")
            elif prompt[0] == 'synDiv':
                if len(prompt) == 4:
                    try:
                        if storemode == False:
                            print(mathfunction.synDiv(float(prompt[1]), eval(prompt[2]))[eval(prompt[3])])
                        elif storemode == True:
                            var = input("Var: ")
                            if len(var) == 1 and var not in invalidvar and var not in storagevar:
                                exec(f"{var} = {mathfunction.synDiv(float(prompt[1]), eval(prompt[2]))[eval(prompt[3])]}")
                                storagevar.append(var)
                                storageval.append(f'function.synDiv({float(prompt[1])}, {eval(prompt[2])})[{eval(prompt[3])}]')
                            else:
                                print("VarError: Variable already exists. Try using delete to remove variable")
                    except ValueError:
                        print("FunctionError: Function only accepts numbers for parameters B and RES, and lists for parameter POLY")
                    except IndexError:
                        print("FunctionError: Invalid input value")
                    except SyntaxError:
                        print("FunctionError: Invalid parameter syntax")
                    except TypeError:
                        print("FunctionError: Function only accepts numbers for parameters B and RES, and lists for parameter POLY")
                else:
                    print("FunctionError: Function uses 3 parameters")
            elif prompt[0] == 'fac':
                if len(prompt) == 2:
                    try:
                        if storemode == False:
                            print(mathfunction.fac(int(prompt[1])))
                        elif storemode == True:
                            var = input("Var: ")
                            if len(var) == 1 and var not in invalidvar and var not in storagevar:
                                exec(f"{var} = {mathfunction.fac(int(prompt[1]))}")
                                storagevar.append(var)
                                storageval.append(f'fac({int(prompt[1])})')
                            else:
                                print("VarError: Variable already exists. Try using delete to remove variable")
                    except ValueError:
                        print("FunctionError: Function only accepts numbers for parameter NUM")
                    except IndexError:
                        print("FunctionError: Invalid input value")
                    except TypeError:
                        print("FunctionError: Function only accepts numbers for parameter NUM")
                else:
                    print("FunctionError: Function uses 1 parameter")
            elif prompt[0] == 'tylrcos':
                if len(prompt) == 2:
                    try:
                        if storemode == False:
                            print(mathfunction.cos(eval(prompt[1])))
                        elif storemode == True:
                            var = input("Var: ")
                            if len(var) == 1 and var not in invalidvar and var not in storagevar:
                                exec(f"{var} = {mathfunction.cos(eval(prompt[1]))}")
                                storagevar.append(var)
                                storageval.append(f'function.cos({eval(prompt[1])})')
                            else:
                                print("VarError: Variable already exists. Try using delete to remove variable")
                    except ValueError:
                        print("FunctionError: Function only accepts numbers for parameter TERMS")
                    except IndexError:
                        print("FunctionError: Invalid input value")
                    except TypeError:
                        print("FunctionError: Function only accepts numbers for parameter TERMS")
                else:
                    print('FunctionError: Function uses 1 parameter')
            elif prompt[0] == 'tylrsin':
                if len(prompt) == 2:
                    try:
                        if storemode == False:
                            print(mathfunction.sin(eval(prompt[1])))
                        elif storemode == True:
                            var = input("Var: ")
                            if len(var) == 1 and var not in invalidvar and var not in storagevar:
                                exec(f"{var} = {mathfunction.sin(eval(prompt[1]))}")
                                storagevar.append(var)
                                storageval.append(f'function.sin({eval(prompt[1])})')
                            else:
                                print("VarError: Variable already exists. Try using delete to remove variable")
                    except ValueError:
                        print("FunctionError: Function only accepts numbers for parameter TERMS")
                    except IndexError:
                        print("FunctionError: Invalid input value")
                    except TypeError:
                        print("FunctionError: Function only accepts numbers for parameter TERMS")
                else:
                    print('FunctionError: Function uses 1 parameter')

            elif prompt[0] == 'polyDeriv':
                if len(prompt) == 2:
                    try:
                        if storemode == False:
                            print(mathfunction.polyDeriv(eval(prompt[1])))
                        elif storemode == True:
                            var = input("Var: ")
                            if len(var) == 1 and var not in invalidvar and var not in storagevar:
                                exec(f"{var} = {mathfunction.polyDeriv(eval(prompt[1]))}")
                                storagevar.append(var)
                                storageval.append(f'function.polyDeriv({eval(prompt[1])})')
                            else:
                                print("VarError: Variable already exists. Try using delete to remove variable")
                    except ValueError:
                        print("FunctionError: Function only accepts lists for parameter POLY")
                    except IndexError:
                        print("FunctionError: Invalid input value")
                    except TypeError:
                        print("FunctionError: Function only accepts lists for parameter POLY")
                else:
                    print('FunctionError: Function uses 1 parameter')
            elif prompt[0] == 'lim':
                if len(prompt) == 5:
                    try:
                        if storemode == False:
                            print(mathfunction.lim(eval(prompt[1]), eval(prompt[2]), eval(prompt[3]), prompt[4]))
                        elif storemode == True:
                            var = input("Var: ")
                            if len(var) == 1 and var not in invalidvar and var not in storagevar:
                                exec(f"{var} = {mathfunction.lim(prompt[1], eval(prompt[2]), eval(prompt[3]), prompt[4])}")
                                storagevar.append(var)
                                storageval.append(f'function.lim({prompt[1], eval(prompt[2]), eval(prompt[3]), prompt[4]})')
                            else:
                                print("VarError: Variable already exists. Try using delete to remove variable")
                    except ValueError:
                        print("FunctionError: Function only accepts numbers, '-inf', 'inf' for parameter VAL, lists for parameters POLY1 and POLY2, and 'left', 'right' for parameter DIRECTION")
                    except IndexError:
                        print("FunctionError: Invalid input value")
                    except SyntaxError:
                        print("FunctionError: Invalid parameter syntax")
                    except TypeError:
                        print("FunctionError: Function only accepts numbers, '-inf', 'inf' for parameter VAL, lists for parameters POLY1 and POLY2, and 'left', 'right' for parameter DIRECTION")
                else:
                    print("FunctionError: Function uses 4 parameters")
            elif prompt[0] == 'rieSum':
                if len(prompt) == 5:
                    try:
                        if storemode == False:
                            print(mathfunction.RieSum(float(prompt[1]), float(prompt[2]), eval(prompt[3]), float(prompt[4])))
                        elif storemode == True:
                            var = input("Var: ")
                            if len(var) == 1 and var not in invalidvar and var not in storagevar:
                                exec(f"{var} = {mathfunction.RieSum(float(prompt[1]), float(prompt[2]), eval(prompt[3]), float(prompt[4]))}")
                                storagevar.append(var)
                                storageval.append(f'function.RieSum(float(prompt[1]), float(prompt[2]), eval(prompt[3]), float(prompt[4])')
                            elif var in invalidvar:
                                print(f"VarError: Invalid variable name. Character {var} cannot be used")
                            elif var in storagevar:
                                print("VarError: Variable already exists. Try using delete to remove variable")
                    except ValueError:
                        print("FunctionError: Function only accepts real numbers for parameters LB, UB, and DX, and lists for parameter POLY")
                    except IndexError:
                        print("FunctionError: Invalid input value")
                    except SyntaxError:
                        print("FunctionError: Invalid parameter syntax")
                    except TypeError:
                        print("FunctionError: Function only accepts real numbers for parameters LB, UB, and DX, and lists for parameter POLY")
                else:
                    print("FunctionError: Function uses 4 parameters")
            elif prompt[0] == 'ln':
                if len(prompt) == 3:
                    try:
                        if storemode == False:
                            print(mathfunction.ln(float(prompt[1]), int(prompt[2])))
                        elif storemode == True:
                            var = input("Var: ")
                            if len(var) == 1 and var not in invalidvar and var not in storagevar:
                                exec(f"{var} = {mathfunction.ln(float(prompt[1]), int(prompt[2]))}")
                                storagevar.append(var)
                                storageval.append(f'mathfunction.ln(int(prompt[1]), float(prompt[2]))')
                            elif var in invalidvar:
                                print(f"VarError: Invalid variable name. Character {var} cannot be used")
                            elif var in storagevar:
                                print("VarError: Variable already exists. Try using delete to remove variable")
                    except ValueError:
                        print("FunctionError: Function only accepts integers for parameter TERMS")
                    except IndexError:
                        print("FunctionError: Invalid input value")
                    except SyntaxError:
                        print("FunctionError: Invalid parameter syntax")
                else:
                    print("FunctionError: Function uses 1 parameter")
            elif prompt[0] == 'exit':
                calcbreaker = False
            else:
                try:
                    if storemode == False:
                        print(eval(''.join(prompt)))
                    else:
                        var = input("Var: ")
                        if len(var) == 1 and var not in invalidvar and var not in storagevar:
                            exec(f"{var} = {eval(''.join(prompt))}")
                            storagevar.append(var)
                            storageval.append(f"{''.join(prompt)}")
                except Exception:
                        print("OptionError: Option does not exist or invalid statement")
    elif prompt[0] == 'graph':
        while True:
            try:
                dx = float(input("Interval for dx: "))
            except ValueError:
                print("ValueError: Only real numbers are acceptable for parameter 'dx'")
                break
            try:
                span = int(input("Span of graph: "))
            except ValueError:
                print("ValueError: Only integers are acceptable for parameter 'span'")
                break
            try:
                xticks = int(input("Number of ticks on the x axis: "))
            except ValueError:
                print("ValueError: Only integers are acceptable for parameter 'xticks'")
                break
            try:
                p = eval(input("Graphed polynomial: "))
                mathfunction.synDiv(1, p)
            except ValueError:
                print("ValueError: Only polynomials in list form are acceptable for parameter 'p'")
                break
            except TypeError:
                print("SyntaxError: Invalid parameter syntax for parameter 'p'")
                break
            graphname = str(input('Name of graph image file (.png already included): '))
            if len(graphname) == 0:
                print("SyntaxError: Filename cannot be 0 characters long")
                break
            iname = str(input('Independent variable: '))
            oname = str(input('Dependent variable: '))
            graphtitle = str(input('Title of graph: '))
            precondition = str(input('Graph condition(s): '))
            postcondition = ''
            for i in range(len(precondition)):
                if precondition[i] == 'x':
                    postcondition = postcondition + '(dx + dx*i)'
                elif precondition[i] == 'y':
                    postcondition = postcondition + 'mathfunction.synDiv(dx + dx*i, p)[1]'
                else:
                    postcondition = postcondition + precondition[i]
            try:
                inte = [dx + dx*i for i in range(int(span/dx)) if eval(postcondition)]
                output = [mathfunction.synDiv(dx + dx*i, p)[1] for i in range(int(span/dx)) if eval(postcondition)]
            except SyntaxError:
                print("SyntaxError: Invalid syntax for graph condition(s)")
                break
            plt.title(f"{graphtitle}")
            plt.xlabel(f"{iname}")
            plt.ylabel(f"{oname}")
            plt.plot(inte, output)
            plt.savefig(f"{graphname}")
            print('==================graphed==================')
            break
    elif prompt[0] == 'exit':
        breaker = False
    elif prompt[0] == 'credits':
        print(credits)
    else:
        print("OptionError: Option does not exist")

#acc = 30
#step = 0.1
#span = 25
#xticks = 6
#precondition = '...'
#postcondition = ''
#for i in range(len(precondition)):
    #if precondition[i] == 'x':
        #postcondition = postcondition + '(dx + dx*i)'
    #elif precondition[i] == 'y':
        #postcondition = postcondition + 'function.synDiv(dx + dx*i, p)'
    #else:
        #postcondition = postcondition + precondition[i]
#try:
    #eval(postcondition)
#except SyntaxError:
    #print("SyntaxError: Invalid syntax for graph condition")
#inte = [dx + dx*i for i in range(int(span/step)) if eval(postcondition)]
#output = [synDiv(dx + dx*i, p)[1] for i in range(int(span/step)) if eval(postcondition)]
#plt.title("f(x) = ...")
#plt.xlabel("x")
#plt.ylabel("f(x)")
#plt.plot(inte, output)
#plt.savefig("Graph")