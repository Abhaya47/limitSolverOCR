import sys
import base64
from sympy import symbols, Limit,sin,cos,tan,ln,log,sqrt,pi
from sympy.parsing.latex import parse_latex
from latex2sympy2 import latex2sympy, latex2latex

def solve(function_string):
    # Prompt the user to enter a function
    # function_string = input("Enter a function: ")
    # function_string=r"{e^x}-{x}\lim \limits _ { x \rightarrow 0 } \frac { \sin x } { x }"
    # function_string=function_string.encode('unicode_escape').decode('utf-8')
    # print(function_string)
    temp=function_string.split(r"\rightarrow")
    tempa=temp[1]
    # print(tempa[1].split)

    temp=temp[1].split("}")


    value=temp[0]
    value=value.strip()

    temp=temp[1:]
    expr='}'.join(temp)
    try:
        expr = latex2sympy(expr)
    except:
        print("Oops Invalid Equation")
    expr=str(expr)
    x = symbols('x')
    f = eval(expr)
    # print(expr)
    if(value=="\infty"):
	# Calculate the limit as x approaches infinity
        limit_inf = Limit(f, x, 'oo').doit()
        print("Limit to infinity:", limit_inf)
    else:
        # Calculate the limit as x approaches a certain value
        value = float(value)
        limit_val = Limit(f, x, value).doit()
        print("Limit to a" + value  +":", limit_val)

argument = sys.argv
new=base64.b64decode(argument[1]).decode('utf-8')
latex=solve(new)
