# progrsm to create simple calculator.

a=int(input("enter First number:"))
b=int(input("enter second number:"))
c=input("enter the operator(+,-,*,/,%):")
if c == "+":
    print("sum of",a, "and ",b,":",a+b)
elif  c == "-":
    print("difference of",a, "and ",b,":",a-b)
elif  c == "*":
    print("multiplication of",a, "and ",b,":",a*b)
elif  c == "/":
    print("division of",a, "and ",b,":",a/b)
elif  c == "%":
    print("modulus of",a, "and ",b,":",a%b)
else:
    print("please choose the correct operator")