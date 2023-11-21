def synDiv(B, Poly):
    bd = 0
    qPoly = []
    for coeff in Poly:
        qPoly.append(coeff + bd)
        bd = B*(coeff + bd)
    return qPoly, qPoly[-1]

def polyMult(l):
    add = [1, -l[0]]
    del(l[0])
    for i in range(len(l)):
        temp = [item*-l[i] for item in add]
        temp.reverse()
        temp.append(0)
        temp.reverse()
        add.append(0)
        add = [add[i]+temp[i] for i in range(len(add))]
    return add

def fac(num):
    result = 1
    for i in range (1, num+1):
        result *= i
    return result

def cos(acc):
    poly = []
    add = 0
    mult = 1
    for i in range(acc):
        poly.append(mult/fac(add))
        poly.append(0)
        add += 2
        mult *= -1
    poly.reverse()
    return poly

def sin(acc):
    poly = [0]
    add = 1
    mult = 1
    for i in range(acc):
        poly.append(mult/fac(add))
        poly.append(0)
        add += 2
        mult *= -1
    poly.reverse()
    return poly

def arccos(acc): #Only when |x| < 1
    poly = []
    for i in range(acc):
        poly.append(0)
        poly.append(-(0.5**i)/(fac(i)+(2*i*fac(i))))
    poly.reverse()

def polyDeriv(poly):
    degsub = 0
    result = poly
    for coeff in result:
        degsub += 1
        if len(result) - degsub != 0:
            result[degsub - 1] *= len(result) - degsub
    del result[-1]
    if len(result) == 0:
        result.append(0)
    return result

def lim(poly1, poly2, app, dr):
    try:
        eval(app)
    except Exception:
        None
    if len(poly1) < len(poly2) and (app == 'inf' or '-inf'):
        return 0
    elif len(poly1) > len(poly2) and (app == 'inf' or app == '-inf'):
        return app
    elif len(poly1) == len(poly2):
        None
    elif synDiv(app, poly2)[1] == 0:
        if dr == 'left':
            if poly1[0] < 0:
                return 'inf'
            else:
                return '-inf'
        if dr == 'right':
            if poly1[0] < 0:
                return '-inf'
            else:
                return 'inf'
    while len(poly2) != 1 or len(poly1) != 1:
        poly1 = polyDeriv(poly1)
        poly2 = polyDeriv(poly2)
    return synDiv(app, poly1)[1]/synDiv(app, poly2)[1]

def RieSum(lb, ub, poly, dx):
    sum = 0
    for i in range(int((ub-lb)/dx)):
        sum += (synDiv(lb + dx*i, poly)[1])
    return sum*dx

def ln(num, acc): #Doesn't currently work with complicated graphs
    result = 0
    power_input = (num-1) / (num+1)
    for i in range(0, int((acc*num)//1)):
        result += (power_input**(2*i + 1))/(2*i + 1)
    return result*2

def e(acc):
    euler = 0
    for i in range (0, acc):
        euler += (1)/(fac(i))
    return euler

def pi(acc):
    c_ratio = 0
    top = 1
    for i in range(0, acc):
        c_ratio += top/(2*i + 1)
        top *= -1
    return 4*c_ratio

print(cos(30))
print()
print(synDiv(3.14159, cos(30)))