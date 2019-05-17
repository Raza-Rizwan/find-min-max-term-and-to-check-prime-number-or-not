#Calculator
def calculator(a,b,c):
        if c=='1':
            return a+b
        elif c=='2':
            return a-b
        elif c=='3':
            return a*b
        elif c=='4':
            return a%b
        elif c=='5':
            return sqrt(a)
firstnumber=float(input("Please Enter a First Number"))
secondnumber=float(input("Please Enter a SEcond number"))
print("Operation Are")
print("1 for Addition")
print("2 for Subraction")
print("3 for Multiplication")
print("4 for Devision")
print("5 for SquareRoot")
c=input("input Selection")
total=calculator(firstnumber,secondnumber,c)
print('Output is:'+str(total))


      