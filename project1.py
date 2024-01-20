import math
def exp(x):
    return math.exp(x)
def derivative(f, formula, x):
    h = 0.05
    fi = f(x)
    fi_1 = f(x-h)
    fi_2 = f(x-2*h)
    fi_3 = f(x-3*h)
    if formula == 'forward':
        return (f(x+h) - fi) / h
    elif formula == 'central':
        return (fi_1 - 2*fi + fi_2) / (2*h)
    elif formula == 'backward':
        return (3*fi - 3*fi_1 + fi_2 - fi_3) / (3*h)
xi = [0.1 + 0.05 * i for i in range(5)]
yi = [exp(x) for x in xi]
dfwd = [derivative(exp, 'forward', xi[i]) for i in range(5)]
dccent = [derivative(exp, 'central', xi[i]) for i in range(5)]
dback = [derivative(exp, 'backward', xi[i]) for i in range(5)]
e_fwd = [abs(dfwd[i] - exp(xi[i])) for i in range(5)] 
e_cent = [abs((dccent[i] - dfwd[i]) / 2) for i in range(5)] 
e_back = [abs((dback[i] - dfwd[i]) / 6) for i in range(5)] 
print("Function values:") 
for i, y in enumerate(yi): 
        print("{:.4f}".format(y))
        print("Derivatives using forward formula:")
for i, d in enumerate(dfwd): 
        print("{:.4f}".format(d)) 
        print("Derivatives using central formula:")
for i, d in enumerate(dccent):
        print("{:.4f}".format(d))
        print("Derivatives using backward formula:")
for i, d in enumerate(dback): 
        print("{:.4f}".format(d))
        print("Errors of differentiation using forward formula:")
for i, e in enumerate(e_fwd): 
        print("{:.4f}".format(e))
        print("Errors of differentiation using central formula:")
for i, e in enumerate(e_cent): 
        print("{:.4f}".format(e))
        print("Errors of differentiation using backward formula:")  
for i, e in enumerate(e_back):
        print("{:.4f}".format(e))  
